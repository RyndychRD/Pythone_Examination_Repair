import os
from zipfile import ZipFile
import shutil


for package in os.listdir(os.getcwd()+'/data'):
	package_name = 'data/'+package
	package_temp_name='temp'
	package_res_name='test'
	password_zip = 'Moreum saver'

	zip_file = ZipFile(package_name)
	zip_file.setpassword(password_zip)

	os.mkdir(package_temp_name) 
	for item in zip_file.infolist():
		filepath = item.filename
		filename = os.path.basename(filepath)
		unzip_test = zip_file.read(filepath, pwd=password_zip)
		unpack_test = open(package_temp_name+"/"+filename, 'wb+')
		unpack_test.write(unzip_test)
		unpack_test.close()

	f=open(package_temp_name+'/res')

	for line in f:
		if line[0]=="{":
			line=line.strip()
			print(line[1:len(line)-1])
	package_res_name=line

	package_res_name=str(package_res_name)

	shutil.move(package_temp_name,package_res_name)


