#TODO unpack dat, find key, unpack di3, in res find studetn, connect to file base, read UID, rename folder, put it on ftp
import os
from zipfile import ZipFile
from Crypto.Cipher import AES

package_name = 'data/didpack.dat'
password_zip = b'\xF1\xE0\x31\x44\x6F\xF1\xCF\x32\x47\xF5\x6F\xCD\xC0\xE2\xE0\xF0\x33\xE8'
print password_zip.decode('UTF 32')
key_aes = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
mode = AES.MODE_ECB
zip_file = ZipFile(package_name)
zip_file.setpassword(password_zip)

for item in zip_file.infolist():
    if '.dat' in item.filename:
        filepath = item.filename
        break

filename = os.path.basename(filepath)
unzip_test = zip_file.read(filepath, pwd=password_zip)

decryptor = AES.new(key_aes, mode)
encrypt_data = unzip_test[4:]
decrypt_data = decryptor.decrypt(encrypt_data)
unpack_test = open(filename, 'wb+')
unpack_test.write(decrypt_data)
unpack_test.close()
