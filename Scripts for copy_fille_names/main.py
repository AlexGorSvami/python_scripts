import os

print('Current folder', os.getcwd())  # проверка текущей директории

path = '/home/alex/Видео/Online courses'  # папка из которой берем файлыз
os.chdir(path)  # меняем текущую директорию на ту, куда указывает путь

print('Current directory', os.getcwd())  # проверка правильности нового пути

list_of_courses = os.listdir()  # получение списка из названий всех фалов
size_sorted_list = sorted(list_of_courses, key=os.path.getsize)  # сортируем список по размеру фалов
with open('List_of_courses', 'w') as f:
    for number, name in enumerate(size_sorted_list):
        f.write(str(number+1) + '. ' + name + '\n')  # записываем в файл

print('File is writed')