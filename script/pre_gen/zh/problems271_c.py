#问题陈述
#高桥要读一个系列漫画 "Snuke-kun"，共10^9卷。
#最初，高桥有这个系列的N本书。  第i本是a_i卷。  
#高桥在开始阅读之前，可以重复以下操作任意次数（可能为零）：
#如果他有1本或更少的书，就什么都不做；否则，就卖掉他有的两本书，买一本任何卷的书来代替。
#然后，高桥按顺序阅读第一卷，第二卷，第三卷，......。  然而，当他没有下一卷的书可读时，他就停止阅读这个系列（不管他有多少卷）。  
#找到他能读到的最新一卷系列书。  如果他不能读任何书，那么答案为0。
#
#限制条件
#1 ≦ N ≦ 3 × 10^5
#1 ≦ a_i ≦ 10^9
#输入的所有数值都是整数。
#
#输入
#输入来自标准输入，其格式如下：
#N
#a_1 ... a_N
#
#輸出
#打印答案。
#
#输入样本1
#6
#1 2 4 6 7 271
#
#样本输出1
#4
#在他开始阅读这套书之前，他可以做以下操作："卖掉第7卷和第271卷的书，买一本第3卷的书代替。"  然后，他拥有第1、2、3、4、6卷各一本。
#如果他开始读这套书，他读了第1、2、3、4卷，然后试图读第5卷。  然而，他没有，所以他在这时停止阅读。
#无论在操作中如何选择，他都无法阅读第5卷，所以答案是4。
#
#样本输入2
#10
#1 1 1 1 1 1 1 1 1 1
#
#样本输出2
#5
#高桥可能有同一卷的多本书。
#对于这个输入，如果他在开始阅读这套书之前进行以下4个操作，他最多可以读到第5卷，这是最大值：
#卖掉第一卷的两本书，改买第二卷的一本书。
#卖掉第一卷的两本书，然后买一本第三卷的书。
#卖掉第一卷的两本书，然后买一本第四卷的书。
#卖两本第一卷，买一本第五卷。
#
#输入样本3
#1
#5
#
#采样输出3
#0
#高桥无法读取第一卷。

def 