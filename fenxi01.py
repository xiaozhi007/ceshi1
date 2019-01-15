#coding=utf-8
import numpy as np
import os
from matplotlib import pyplot  as plt

data_path='./bikeshare'
data_filepath= ['2017-q1_trip_history_data.csv', '2017-q2_trip_history_data.csv',
                  '2017-q3_trip_history_data.csv', '2017-q4_trip_history_data.csv']


def  shoujidata():
    data_arr_list=[]
    for data_filename in data_filepath:
        ####路径拼接
        data_file=os.path.join(data_path,data_filename)
        data_arr=np.loadtxt(data_file,delimiter=',',dtype='str',skiprows=1)
        data_arr_list.append(data_arr)
    return data_arr_list

def  chulidata(data_arr_list):
    chuli_datalist=[]
    for data_arr in  data_arr_list:
        ####列操作，替换字符操作！！！！！
        temp_data=np.core.defchararray.replace(data_arr[:,0],'"','')
        chuli_datalist.append((temp_data.astype('float')/1000/60))
    return chuli_datalist
def  fenxidata(data_arr_list):
    chuli_data=[]
    ####利用enumerate()导入列表可以返回两个参数，一个是循环索引值，也就是取值索引编号。
    ####另一个是与索引对应的列表值
    for i,data in enumerate(data_arr_list):
        print('第{}季度的平均骑行时间：{:.2f}分钟'.format(i+1,np.mean(data)))
        chuli_data.append(np.mean(data))
    return chuli_data

def  huitudata(chuli_data):
    plt.figure(figsize=(20,8),dpi=80)
    plt.bar(range(len(chuli_data)),chuli_data)
    plt.show()
    
    
    
    

def  main():
    data_arr_list=shoujidata()
    chuli_datalist=chulidata(data_arr_list)
    chuli_data=fenxidata(chuli_datalist)
    huitudata(chuli_data)


if __name__=="__main__":
    main()





