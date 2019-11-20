import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class DataGenerator(object):
    def __init__(self):
        # 函数方程式
        # 变量用x, y
        self.func = ""

    def _replace(self):
        """替换公式中的一些函数"""
        self.func = self.func.replace('exp', 'np.exp')
        self.func = self.func.replace('ln', 'np.log2')
        self.func = self.func.replace('lg', 'np.log10')

    def set_func(self, func_str):
        self.func = func_str
        self._replace()

    def generate(self, low=(0, 0), up=(100, 100)):
        """生成一个数据集"""
        X = np.linspace(low[0], up[0], num=50)
        Y = np.linspace(low[1], up[1], num=50)
        x, y = np.meshgrid(X, Y)
        z = eval(self.func)
        print(z)
        return x, y, z

    def calculate(self, x, y):
        return eval(self.func)


if __name__ == "__main__":
    dg = DataGenerator()
    function = "- x * x  - y * y"
    dg.set_func(function)
    x, y, z = dg.generate(low=(-10, -10), up=(10, 10))
    ax = Axes3D(plt.figure())
    ax.plot_surface(x, y, z, cmap="rainbow")
    plt.show()
    print("x = 5, y = 4, z =", dg.calculate(5, 4))
