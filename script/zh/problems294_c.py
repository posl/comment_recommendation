#问题陈述
#给你长度为N和M的严格递增序列：A=(A _ 1,A _ 2,...,A _ N)和B=(B _ 1,B _ 2,...,B _ M)。
#这里，对于每一个i和j，A _ i≠B _ j（1≦ i≦ N,1≦ j≦ M）。
#让C=(C _ 1,C _ 2,...,C _ {N+M})是一个长度为N+M的严格递增序列，由以下程序产生。
#形式上，让C _ i=A _ i for i=1,2,...,N, and C _ i=B _ {i-N} for i=N+1,N+2,...,N+M。
#将C按升序排序。
#对于A _ 1,A _ 2,...,A _ N, B _ 1,B _ 2,...,B _ M中的每一个，找出它在C中的位置。
#更确切地说，对于每个i=1,2,...,N，找到k，使C _ k=A _ i，对于每个j=1,2,...,M，找到k使C _ k=B _ j。
#
#限制条件
#1≦ N,M≦ 10^5
#1≦ a _ 1< a _ 2<...< a _ n≦ 10^9
#1≦ b _ 1< b _ 2<...< b _ m≦ 10^9
#对于每个i和j，A _ i≠B _ j (1≦ i≦ N,1≦ j≦ M)。
#输入的所有数值都是整数。
#
#输入
#输入来自标准输入，其格式如下：
#N M
#A _ 1 A _ 2 ...A _ N
#B _ 1 B _ 2 ...B _ M
#
#输出
#分两行打印答案。
#第一行应该包含C中A _ 1,A _ 2,...,A _ N的位置，中间有空格。
#第二行应该包含B _ 1,B _ 2,...,B _ M在C中的位置，中间有空格。  
#
#输入样本 1
#4 3
#3 14 15 92
#6 53 58
#
#样本输出1
#1 3 4 7
#2 5 6
#C将是（3,6,14,15,53,58,92）。
#这里，第1，3，4，7个元素来自A=（3，14，15，92），第2，5，6个元素来自B=（6，53，58）。
#
#样本输入 2
#4 4
#1 2 3 4
#100 200 300 400
#
#样本输出 2
#1 2 3 4
#5 6 7 8
#
#样本输入3
#8 12
#3 4 10 15 17 18 22 30
#5 7 11 13 14 16 19 21 23 24 27 28
#
#样本输出3
#1 2 5 9 11 12 15 20
#3 4 6 7 8 10 13 14 16 17 18 19

def 