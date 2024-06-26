#问题陈述
#我们有一个有H个水平行和W个垂直列的网格。  (i, j)表示从上往下第i行和从左往下第j列的方格。
#(i,j)上写有一个字符G_{i,j}。  G_{i,j}是U、D、L或R。
#你最初是在（1,1）。  你重复以下操作，直到你无法下棋为止。
#设(i,j)为你目前所在的方格。
#如果G_{i,j}是U且i≠1，则移动到（i-1,j）。
#如果G_{i,j}是D，且i≠H，则移动到（i+1,j）。
#如果G_{i,j}是L且j≠1，则移动到（i,j-1）。
#如果G_{i,j}是R且j≠W，则移动到（i,j+1）。
#否则，你不能走棋。  
#打印你在无法下棋时最终所处的位置。
#如果你无限期地重复移动，则打印-1来代替。
#
#限制条件
#1 ≦ H, W ≦ 500
#G_{i,j}是U, D, L, 或R。
#H和W是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#H W
#G_{1,1}G_{1,2}...G_{1,W}
#G_{2,1}G_{2,2}...G_{2,W}
#.
#.
#.
#G_{H,1}G_{H,2}...G_{H,W}
#
#输出
#如果你在(i, j)处结束，请按以下格式打印：
#i j
#如果你无限期地重复移动，则打印-1。
#
#输入样本 1
#2 3
#RDU
#LRU
#
#样本输出1
#1 3
#你将以（1，1）->（1，2）->（2，2）->（2，3）->（1，3）的方式移动，最后在这里结束，所以答案是（1，3）。
#
#输入样本 2
#2 3
#RRD
#超低频
#
#样本输出2
#-1
#你将无限期地重复移动，如（1，1）->（1，2）->（1，3）->（2，3）->（2，2）->（2，1）->（1，1）->（1，2）->...，所以在这种情况下应该打印-1。
#
#输入样本 3
#9 44
#rrddddrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
#rrrdlrdllllrdrldrdrdllllldrdtd
#drdlrrdlrdrldrldrldrldrldrldrldrldrldrldrldrldrldrldrldrldrldrldrldrldrldrldrldrldrldrrdrldrd
#
#
#
#rdlrrdlrdrlrdrddrrdrdlrdrrdrrrr
#rdldrrldrlllldrdrlllldrdrlllldrdrlllldrdrlllldrdrlldrdrlldrdrlldrdrlldrdrlldrdrlldrdrlldrdrlldrdrlldrdrlldrdrlltd
#
#
#样本输出3
#9 5

def 