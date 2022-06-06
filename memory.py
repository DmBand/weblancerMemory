import psutil
import datetime

with open('file.txt', 'a') as f:
    f.write(f'===== {datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")} =====\n')
    memory = psutil.virtual_memory()
    virtual_memory_available = f'{round(memory[1] / (1024 ** 2), 1)} mb | {round((memory[1] / (1024 ** 3)), 1)} gb'
    virtual_memory_total = f'{round(memory[0] / (1024 ** 2), 1)} mb | {round((memory[0] / (1024 ** 3)), 1)} gb'
    f.write(f'Доступно ОЗУ: {virtual_memory_available}\n'
            f'Общий объем ОЗУ: {virtual_memory_total}\n')
    using_memory = memory[2]
    if using_memory > 20:
        f.write(f'ВНИМАНИЕ, использование ОЗУ составляет {using_memory}%\n')
    hdds = [d for d in psutil.disk_partitions(False) if d[2]]
    for i in hdds:
        f.write(f'Доступное место на диске {i[1]}: {round((psutil.disk_usage(i[1])[2] / (1024 ** 2)), 1)} mb | '
                f'{round((psutil.disk_usage(i[1])[2] / (1024 ** 3)), 1)} gb\n')
        if psutil.disk_usage(i[1])[3] > 20:
            f.write(f'ВНИМАНИЕ, диск {i[1]} заполнен на {psutil.disk_usage(i[1])[3]}%\n')
    f.write('\n\n')
