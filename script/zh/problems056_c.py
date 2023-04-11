#问题陈述
#在一条从左到右的无限长的数轴上，有一只袋鼠位于坐标0处，时间为0。
#在时间i-1和时间i之间，袋鼠可以停留在他的位置上，也可以向左或向右做长度正好为i的跳跃。
#也就是说，如果他在i-1时间的坐标是x，他在i时间可以在坐标x-i，x或x+i。
#袋鼠的巢穴在坐标X处，他想尽可能快地前往坐标X。
#请找出最早到达坐标X的时间。
#
#约束条件
#X是一个整数。
#1≤X≤10^9
#
#输入
#输入来自标准输入，其格式如下：
#X
#
#输出
#打印袋鼠到达坐标X的最早可能时间。
#
#输入样本1
#6
#
#样本输出1
#3
#袋鼠通过向右跳动三次，可以在时间3到达他的巢穴，这是最早的可能时间。
#
#样本输入2
#2
#
#样本输出 2
#2
#他可以在时间2到达他的巢穴，方法是在第一秒内停留在他的位置，并在下一秒内跳到右边。
#
#输入样本3
#11
#
#样本输出3
#5

def 