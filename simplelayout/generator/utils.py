"""
辅助函数
"""

from pathlib import Path
import matplotlib.pyplot as plt
from scipy.io import savemat
import os


def save_matrix(matrix, file_name):
    # TODO: 存储 matrix 到 file_name.mat, mdict 的 key 为 "matrix"
    mdict = {"matrix": matrix}
    savemat("file_name.mat", mdict)


def save_fig(matrix, file_name):
    # TODO: 将 matrix 画图保存到 file_name.jpg
    plt.imshow(matrix)
    plt.savefig(filename)


def make_dir(outdir):
    # TODO: 当目录 outdir 不存在时创建目录
    if not os.path.exists(outdir):
        os.makedirs(outdir)
