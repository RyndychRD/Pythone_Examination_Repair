import subprocess
import os
from zipfile import ZipFile
import shutil

#объявление переменных

package_temp_name='temp'
package_res_name='test'
package_error_name='!ERROR'
password_zip = 'Moreum saver'
password_zip =bytes(password_zip, 'utf-8')
package_output_name='!RESULT'
	

#результаты будут в папке result
if  not os.path.exists(package_output_name):
		os.mkdir(package_output_name) 
#удаление мусора с предыдущей работы программы
if os.path.exists(package_temp_name):
	path = os.path.join(os.path.abspath(os.path.dirname(__file__)), package_temp_name)
	shutil.rmtree(path) 		
#для всех файлов в папке проверяется на то, что они di3 и разархивируется, иначе переходит к следующему файлу
#файлы берутся из папки data
for package in os.listdir(os.getcwd()+'/data'):
	if '.di3' in package:			
		package_name = 'data/'+package
		zip_file = ZipFile(package_name)
		zip_file.setpassword(password_zip)
		#создание временной папки и разархивирование туда содержимого архива
		if  not os.path.exists(package_temp_name):
			os.mkdir(package_temp_name) 
			for item in zip_file.infolist():
				try:
					filepath = item.filename
					filename = os.path.basename(filepath)
					unzip_test = zip_file.read(filepath, pwd=password_zip)
					unpack_test = open(package_temp_name+"/"+filename, 'wb+')
					unpack_test.write(unzip_test)
					unpack_test.close()
				except:
				#если не удается распаковать, кидаем в error 
					if  not os.path.exists(package_error_name):
						os.mkdir(package_error_name)
					os.rename(package,package_error_name+'/'+package)
				else:

					#Считывание имя файла, который должен быть в системе дистанционки
					f=open(package_temp_name+'/res','r',encoding='cp1251')
					for line in f:
						if line[0]=="{":
							line=line.strip()
							print(line[1:len(line)-1])
							line=line[1:len(line)-1]
							package_res_name=line	
					
					f.close()
					#переименование временного файла в нужный
					if  not os.path.exists(package_output_name+'/'+package_res_name):
						os.rename(package_temp_name,package_output_name+'/'+package_res_name)

#удаление мусора с предыдущей работы программы
if os.path.exists(package_temp_name):
	path = os.path.join(os.path.abspath(os.path.dirname(__file__)), package_temp_name)
	shutil.rmtree(path) 		
