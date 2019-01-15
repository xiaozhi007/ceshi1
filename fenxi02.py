#coding=utf-8

import numpy as np
from matplotlib import pyplot as plt
import os


data_path='./bikeshare'
data_filepath= ['2017-q1_trip_history_data.csv', '2017-q2_trip_history_data.csv',
                  '2017-q3_trip_history_data.csv', '2017-q4_trip_history_data.csv']



def  shouji_qingxi_data():
    data_arr_list=[]
    for data_filename in data_filepath:
        ####路径拼接
        data_file=os.path.join(data_path,data_filename)
        data_arr=np.loadtxt(data_file,delimiter=',',dtype='str',skiprows=1)

        qingxi_data=np.core.defchararray.replace(data_arr,'"','')
        data_arr_list.append(qingxi_data)
    return data_arr_list

def fenxi_data(a,member_type):
    mean_data=[]
    for j,i in enumerate(a):
        ####利用布尔型数组筛选数组
        ####利用数组比较的广播性进行判断对比
        kk=i[i[:,-1]==member_type]
        ss=np.mean(kk[:,0].astype("float")/1000/60)
        mean_data.append(ss)
        print("{}会员第{}季度的平均骑行时间为：{:.2f}".format(member_type,j+1,ss))
    return mean_data


def save_show_data(Member_data,Casual_data):
    #此处将数据放入一个列表中，生成ndarray数组类型，同时做一个转置。
    save_data=np.array([Member_data,Casual_data]).T
    #将内容保存到一个csv文件中，并且指定文件名、位置、数据源、分隔符、表头、数字格式，同时设定comments（注释）为空，默认是#
    np.savetxt('./mean_data.csv',save_data,delimiter=',',header='Member,Casual',fmt='%.4f',comments='')
    #创建一个空的画布
    plt.figure()
    plt.plot(Member_data,color='g',linestyle='-',marker='o',label="Member")
    plt.plot(Casual_data,color='r',linestyle='--',marker='*',label="Casual")
    plt.title('Member vs Casual')
    #x轴标签设定
    plt.xticks(range(0,4),['1st','2nd','3rd','4th'],rotation=45)
    plt.xlabel("jidu")
    plt.ylabel('mean')
    plt.legend(loc='best')
    #以紧凑的方式展现
    plt.tight_layout()

    plt.savefig('./Member_vs_Casual.png')
    plt.show()



def main():
    #调用数据收集清洗方法
    a=shouji_qingxi_data()

    #针对两种会员类型，分别调用数据分析函数。
    b1=fenxi_data(a,'Member')
    b2 = fenxi_data(a,'Casual')
    save_show_data(b1,b2)


if __name__=="__main__":
    main()
