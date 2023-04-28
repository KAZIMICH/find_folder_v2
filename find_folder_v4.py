import multiprocessing
import threading
import os
import time
import requirements

# # декоратор измерения времени работы программы
# def timemeter(func):
#     from time import time
#
#     def wrapper(*args):
#         start_time = time()
#         value = func(*args)
#         end_time = time()
#         print(f'Время выполнения функции {end_time - start_time} сек.')
#         return value
#
#     return wrapper


def folders_path(rootdir):
    folder_list = []
    for it in os.scandir(rootdir):
        if it.is_dir():
            folder_list.append(it.path)
    folder_list.pop(0)  # исключаю папку #recycle
    return folder_list


def find_path(folder, path):
    fstart = time.time()
    for root, dirs, files in os.walk(path):
        if folder in dirs:
            path = os.path.join(root, folder)
            print(path)
            break
    print(f'папка по пути {path} отсканирована за')
    fend = time.time()
    print(fend - fstart)


def multiproc(name, path):
    list1 = []
    for i in range(1, len(path)):
        list1.append(f'process{i}')
        # print(list1)

    for i in list1:
        count = 0
        for j in path:
            i = threading.Thread(target=find_path, args=(name, j))
            i.start()
            # i.join()
            count += 1
            print(f'процесс {count} сгенерирован путь {j}')
        if count == len(path):
            print(f'сгенерировано {count} процессов')
            break
        i.join()


if __name__ == "__main__":
    start = time.time()

    target_folder = r'\\192.168.1.98\03_пароходы_чертежи'  # папка поиска
    folders_list = folders_path(target_folder)

    name_folder = 'ICE GRACE'  # искомая папка1

    multiproc(name_folder, folders_list)

    # target_path = find_path(name_folder, target_folder)
    # print(target_path)

    # find_path(name_folder2, target_folder2)

    end = time.time()
    print(end - start)
