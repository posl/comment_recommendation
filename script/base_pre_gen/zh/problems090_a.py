#问题陈述
#我们有一个3×3的方格，每个方格都包含一个小写英文字母。
#位于从上往下第i行、从左往下第j列的方格中的字母是c_{ij}。
#将连接网格左上角和右下角的对角线上的字母连接起来，从左上角到右下角，可以得到长度为3的字符串。
#
#限制条件
#输入的是小写英文字母。
#
#输入
#输入是由标准输入法提供的，格式如下：
#C_{11}C_{12}C_{13}
#C_{21}C_{22}C_{23}
#C_{31}C_{32}C_{33}
#
#输出
#打印长度为3的字符串，该字符串由连接网格左上角和右下角的对角线上的字母连接而成，从左上角到右下角，可以得到。
#
#输入样本1
#蚂蚁
#obe
#记录
#
#样本输出1
#abc
#连接网格左上角和右下角的对角线上的字母从右上角到左下角分别是a、b和c。将这些字母串联起来，打印出abc。
#
#输入样本2
#edu
#貓
#符号
#
#样本输出2
#ean

def 