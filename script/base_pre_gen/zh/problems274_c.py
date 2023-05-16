#问题陈述
#你观察了变形虫并做了一些记录。
#最初，有一个阿米巴虫，编号为1。
#你做了N次记录。根据第i条记录，编号为A_i的变形虫消失了，它自己分成了两个新的变形虫，然后被编号为2i和2i+1。
#这里，阿米巴A_i被说成是阿米巴2i和2i+1的父母。
#对于每个k=1,...,2N+1，变形虫k与变形虫1相距多少代？
#
#限制条件
#1 ≦ N ≦ 2× 10^5
#记录是一致的。就是说：
#1≦ A_i ≦ 2i-1。
#A_i是不同的整数。
#
#
#输入
#输入来自标准输入，其格式如下：
#N
#A_1 A_2 ...A_N
#
#输出
#打印2N+1行。第k行应包含阿米巴1和阿米巴k之间的生成距离。
#
#输入样本 1
#2
#1 2
#
#采样输出1
#0
#1
#1
#2
#2
#从阿米巴1中，诞生了阿米巴2和3。从阿米巴2开始，诞生了阿米巴4和5。
#阿米巴1与阿米巴1是零代的关系。
#阿米巴2与阿米巴1有一代之隔。
#阿米巴3与阿米巴1相距一代。
#阿米巴4与阿米巴2相距一代，与阿米巴1相距两代。
#阿米巴5与阿米巴2相距一代，与阿米巴1相距两代。
#
#样本输入2
#4
#1 3 5 2
#
#样本输出2
#0
#1
#1
#2
#2
#3
#3
#2
#2

def 