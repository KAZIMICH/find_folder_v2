import multiprocessing
import time

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


import multiprocessing
import os
import time


def folders_path(folder_list, rootdir):
    for it in os.scandir(rootdir):
        if it.is_dir():
            folder_list.append(it.path)
    folder_list.pop(0)  # исключаю папку #recycle
    return folder_list


def find_path(name_folder, path):
    for i in folder_list:
        for root, dirs, files in os.walk(path):
            if name_folder in dirs:
                return os.path.join(root, name_folder)
        return None

def sequential(calc, proc):
    print(f"Запускаем поток № {proc}")
    for i in range(calc):
        find_path('ICE GRACE', r'\\192.168.1.98\03_пароходы_чертежи')
    print(f"{calc} циклов вычислений закончены. Процессор № {proc}")


# def heavy(n, i, proc):
#     for x in range(1, n):
#         for y in range(1, n):
#             x ** y
#     print(f"Цикл № {i} ядро {proc}")

#
# def sequential(calc, proc):
#     print(f"Запускаем поток № {proc}")
#     for i in range(calc):
#         heavy(500, i, proc)
#     print(f"{calc} циклов вычислений закончены. Процессор № {proc}")


def processesed(procs, calc):
    # procs - количество ядер
    # calc - количество операций на ядро

    processes = []

    # делим вычисления на количество ядер
    for proc in range(procs):
        p = multiprocessing.Process(target=sequential, args=(calc, proc))
        processes.append(p)
        p.start()

    # Ждем, пока все ядра
    # завершат свою работу.
    for p in processes:
        p.join()


if __name__ == "__main__":
    start = time.time()
    target_folder = r'\\192.168.1.98\03_пароходы_чертежи'
    folder_list = []
    name_folder = 'ICE GRACE'  # искомая папка
    folders_path(folder_list, target_folder)
    print(folder_list)
    # узнаем количество ядер у процессора
    n_proc = multiprocessing.cpu_count()
    # вычисляем сколько циклов вычислений будет приходится на 1 ядро
    # print(folder_list)
    calc = len(folder_list) // n_proc + 1
    processesed(n_proc, calc)
    end = time.time()
    print(f"Всего {n_proc} ядер в процессоре")
    print(f"На каждом ядре произведено {calc} циклов вычислений")
    print(f"Итого {n_proc * calc} циклов за: ", end - start)
