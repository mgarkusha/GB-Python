import os

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

i = 1
curr_dir = os.getcwd()
while i <= 9:
    new_dir = os.path.join(curr_dir, 'dir_' + str(i))
    try:
        os.mkdir(new_dir)
        i += 1
    except:
        break

new_folder_list = []
for i in os.listdir(curr_dir):
    if os.path.isdir(i):
        new_folder_list.append(i)
print('Добавленные директории: ', new_folder_list)

i = 1
while i <= 9:
    os.removedirs('dir_' + str(i))
    i += 1

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

new_folder_list = []
for i in os.listdir(curr_dir):
    if os.path.isdir(i):
        new_folder_list.append(i)
print('Папки текущей директории: ', new_folder_list)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
