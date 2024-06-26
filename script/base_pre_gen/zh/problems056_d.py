#问题陈述
#小鹿AtCoDeer有N张写有正整数的卡片。第i张卡片上的数字（1≤i≤N）是a_i。
#因为他喜欢大数字，所以当子集的卡片上所写的数字之和大于或等于K时，他就称该卡片的子集为好。
#然后，对于每张牌i，他判断它是否是不必要的，如下所示：
#如果对于任何包含卡片i的良好子集，从子集中剔除卡片i后得到的集合也是良好的，那么卡片i就是不必要的。
#否则，第i张牌就不是不必要的。
#找到不必要的牌的数量。在这里，他对每张牌都是独立判断的，而且他不会丢弃那些被证明是不必要的牌。
#
#限制条件
#所有的输入值都是整数。
#1≤N≤5000
#1≤K≤5000
#1≤a_i≤10^9 (1≤i≤N)
#
#部分得分
#通过满足N,K≤400的测试集，可得300分。
#
#输入
#输入是由标准输入给出的，其格式如下：
#N K
#a_1 a_2 ... a_N
#
#输出
#打印不必要的卡的数量。
#
#输入样本 1
#3 6
#1 4 3
#
#样本输出 1
#1
#有两个好的集合：{2,3}和{1,2,3}。
#卡片1只包含在{1,2,3}中，而这个没有卡片1的集合，{2,3}，也是好的。因此，牌1是不必要的。
#对于牌2来说，没有牌2的好集合{2,3}，{3}是不好的。因此，牌2不是不必要的。
#同样的原因，牌3也不是，因此答案是1。
#
#输入样本 2
#5 400
#3 1 4 1 5
#
#样本输出2
#5
#在这种情况下，没有好的组合。因此，所有的牌都是不必要的。
#
#样本输入3
#6 20
#10 4 3 10 25 2
#
#样本输出 3
#3

def 