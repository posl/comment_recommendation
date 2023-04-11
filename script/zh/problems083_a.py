#问题说明
#如果L>R，天平向左倾斜，其中L是左盘上质量的总重量，R是右盘上质量的总重量。同样地，如果L=R，它就会平衡，如果L<R，它就会向右倾斜。
#高桥将一个质量为A的砝码和一个质量为B的砝码放在天平秤的左盘上，并将一个质量为C的砝码和一个质量为D的砝码放在右盘上。
#如果天平秤向左倾斜，则打印左；如果平衡，则打印平衡；如果向右倾斜，则打印右。
#
#限制条件
#1≦ a,b,c,d ≦ 10
#所有输入值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#A B C D
#
#输出
#如果天平秤向左倾斜，则打印为左；如果平衡，则打印为平衡；如果向右倾斜，则打印为右。
#
#输入样本 1
#3 8 7 1
#
#输出示例 1
#左边
#左边盘子上的质量的总重量是11，右边盘子上的质量的总重量是8，由于11>8，我们应该打印左。
#
#输入示例 2
#3 4 5 2
#
#样本输出2
#平衡
#左边盘子里的质量总重量是7，右边盘子里的质量总重量是7，由于7=7，我们应该打印平衡。
#
#输入样本3
#1 7 6 4
#
#样本输出3
#对
#左边盘子里的质量总重量是8，右边盘子里的质量总重量是10。由于8<10，我们应该打印右。

def 