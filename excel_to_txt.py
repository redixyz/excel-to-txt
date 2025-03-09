import os
import pandas as pd


files=[i for i in os.listdir(os.getcwd()) if '.xlsx' in i or '.xls' in i]


def excel_to_txt(files):
    for file in files:
        df = pd.read_excel(file, header=None)
        try:
            os.remove(os.path.join(os.getcwd(), file.split('.')[0] + '.txt'))
        except:
            pass
        f = open(file.split('.')[0] + '.txt', 'w+')
        f.close()
        f = open(file.split('.')[0] + '.txt', 'a+')
        for row in df.itertuples(index=False, name=None):
            f.write(" ".join(map(str, row)) + '\n')


def remove_excel(files):
    for file in files:
        try:os.remove(os.path.join(os.getcwd(), file.split('.')[0] + '.txt'))
        except:pass


if __name__=='__main__':
    print('1 - перевести excel файлы в txt')
    print('0 - удалить excel файлы')
    chose=int(input())
    if chose:
        excel_to_txt()
    if not chose:remove_excel()
    print('Готово!')