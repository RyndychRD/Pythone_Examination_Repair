import subprocess
import os
from zipfile import ZipFile
import shutil
#used python-docx 0.8
from docx import Document

document = Document()
# объявление переменных

package_temp_name = 'temp'
package_res_name = 'test'
package_error_name = '!ERROR'
password_zip = 'Moreum saver'
password_zip = bytes(password_zip, 'utf-8')
package_output_name = '!RESULT'

# результаты будут в папке result
if not os.path.exists(package_output_name):
    os.mkdir(package_output_name)
if not os.path.exists(package_error_name):
    os.mkdir(package_error_name)
# для всех файлов в папке проверяется на то, что они di3 и разархивируется, иначе переходит к следующему файлу
# файлы берутся из папки data
for package in os.listdir(os.getcwd() + '/data'):
    if '.di3' in package:
        #	try:
        package_name = 'data/' + package
        zip_file = ZipFile(package_name)
        zip_file.setpassword(password_zip)
        package_res_name = '!RESULT/' + package
        # создание временной папки и разархивирование туда содержимого архива
        if not os.path.exists(package_res_name):
            os.mkdir(package_res_name)
        for item in zip_file.infolist():
            filepath = item.filename
            filename = os.path.basename(filepath)
            unzip_test = zip_file.read(filepath, pwd=password_zip)
            unpack_test = open(package_res_name + "/" + filename, 'wb+')
            unpack_test.write(unzip_test)
            unpack_test.close()

        # Считывание имя файла, который должен быть в системе дистанционки
        f = open(package_res_name + '/que1', 'r', encoding='cp1251')
        document.add_heading('Вопрос 1', level=1)
        for line in f:
            document.add_paragraph(line)
        f.close()

        f = open(package_res_name + '/ans1', 'r', encoding='cp1251')
        document.add_heading('Ответ:', level=1)
        for line in f:
            document.add_paragraph(line)
        f.close()

        f = open(package_res_name + '/que2', 'r', encoding='cp1251')
        document.add_heading('Вопрос 2', level=1)
        for line in f:
            document.add_paragraph(line)
        f.close()

        f = open(package_res_name + '/ans2', 'r', encoding='cp1251')
        document.add_heading('Ответ:', level=1)
        for line in f:
            document.add_paragraph(line)
        f.close()

        document.save(package_res_name + '.docx')
        document = Document()

        # переименование временного файла в нужный
        if os.path.exists(package_res_name):
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), package_res_name)
            shutil.rmtree(path)
    #	except:
#		os.rename(package,package_error_name+'/'+package)

# удаление мусора с предыдущей работы программы
if os.path.exists(package_temp_name):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), package_temp_name)
    shutil.rmtree(path)
