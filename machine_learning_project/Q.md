# 求解思路

### 1. 获取用于训练模型的训练集
- 方法1: csv pandas
- 方法2: MySQL
    - 创建三个表：train，weather, poi
    - 导入数据 csv -> table
    - 关联查询，获取真实的训练集
### 2. 选择合适的算法训练模型
- sk-learn 模块，选择一种算法
- 传入真实的训练集，训练模型
### 3. 将测试集导入模型，获取预测结果
- 将测试集进行类似于训练集同样的处理
- 使用模型，求得结果

### 4. 第三方库

- `conda install numpy`
- `conda install pandas`
- `conda install pymysql`
- `conda install scikit-learn`
