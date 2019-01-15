# 实用python主义三：比较共享单车各种用户类别的比例
# coding=utf-8

import numpy as np
from matplotlib import pyplot as plt
import os

data_path = './bikeshare'
data_filepath = ['2017-q1_trip_history_data.csv', '2017-q2_trip_history_data.csv',
                 '2017-q3_trip_history_data.csv', '2017-q4_trip_history_data.csv']

def shouji_qingxi_data():
    member_type_list = []
    for data_filename in data_filepath:
        data_file = os.path.join(data_path, data_filename)
        data_arr = np.loadtxt(data_file, delimiter=',', dtype='str', skiprows=1)

        # 去掉双引号
        # reshape(-1,1)，当有一个维度参数确定，另一个参数可以用-1代替，python自动补全。
        member_type_col = np.core.defchararray.replace(data_arr[:, -1], '"', '')

        member_type_col = member_type_col.reshape(-1, 1)
        member_type_list.append(member_type_col)
    #用于在行方向上合并数据。
    year_member_list = np.concatenate(member_type_list)
    return year_member_list


def chuli(aa):
    n_member = aa[aa == 'Member'].shape[0]
    n_casual = aa[aa == 'Casual'].shape[0]
    n_uses = [n_member, n_casual]

    return n_uses


def save_show_result(bb):
    plt.figure()
    # 绘制饼状图，autopct以百分比的形式呈现,shadow阴影，explod指定突出
    plt.pie(bb,autopct='%.2f%%',labels=['Member','Casual'],shadow=True,explode=(0.05,0.07))
    plt.tight_layout()
    plt.savefig("./shuchu.png")
    plt.show()

def main():
    aa = shouji_qingxi_data()
    bb = chuli(aa)
    save_show_result(bb)

if __name__ == '__main__':
    main()
