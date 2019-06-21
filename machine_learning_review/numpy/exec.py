from numpy import *  # 不推荐
import matplotlib.pyplot as plt
from numpy.random import rand

# 1. 安装 Numpy
# conda install numpy

# 2. a = [1, 2, 3, 4]，使用 Numpy 将每个元素 + 1
a = [1, 2, 3, 4]
a = array(a)
print(a + 1)

# 3. b = [4, 5, 6, 7]，使用 Numpy 将 a 和 b 对应元素相加
b = [4, 5, 6, 7]
# b=array(b)
print(a + b)

# 4. 将 a 转换为 2×2 的二维数组
a.shape = 2, 2
print(a)

# 5. 根据以下代码绘制曲线图
a = linspace(0, 2*pi, 21)
print(a)
b = sin(a)

# conda install matplotlib
plt.plot(a, b)
# plt.show()

# 6. 选取 b 中所有的非负值
print(b >= 0)

# 7. 绘制 a, b 对应的非负值的点
mask = (b >= 0)
plt.plot(a[mask], b[mask], 'ro')
plt.show()

# 8. 求 a 所有元素的和
# print(a)
print(sum(a))

# 9. 求 a 所有元素乘积
print(prod(a)) # 连乘操作

# 10. 求以下 a 的全局最大最小值
a = rand(3, 4)
print(a)
print('min:', a.min())
print('max:', a.max())

# 11.求 a 的均值
a = array([[1, 2, 3], [4, 5, 6]])
print(a.mean())

# 12. 求 a 的标准差
print(a.std(axis=1))

# 13. 求 a 的方差
print(a.var(axis=1))

# 14. 把 a 限制在 [3,5] 范围内
a = array([[1, 2, 3],
           [4, 5, 6]])
print(a.clip(3, 5)) # 比3小的变成3 比5大的变成5

# 15. 把 a 近似到整数和一位小数
a = array([1.35, 2.5, 1.5])
print(a.round())  # .5 的近似，取向最近的偶数

# print(a.round(decimals=1))
#
# a = arange(6)
# print(a)
#
# a = array([[[0, 1, 2]],
#
#            [[3, 4, 5]]])
#
# print(a.T)

# 16. 把数组修改为 2×3
a = arange(8)
print(a)
a.shape = 2, 4
print(a)

# 17. 对 a 做转置

a = array([[[0, 1, 2]],

           [[3, 4, 5]]])

print(a.transpose())
print(a.T)

# 18. 将 a 转为一维数组

a = array([[0, 1],
           [2, 3]])

print(a.flatten())

# 19. 求 a 的对角线

a = array([11, 21, 31, 12, 22, 32, 13, 23, 33])
a.shape = 3, 3
print(a)
print(a.diagonal())

# 20. 求 a 的右移 1 次对角线
print(a.diagonal(offset=1))
print(a.diagonal(offset=2))
print(a.diagonal(offset=-2))