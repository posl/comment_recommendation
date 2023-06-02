#问题陈述
#给你一个由A、C、G和T组成的长度为N的字符串S，回答以下Q个查询：
#查询i（1 ≦ i ≦ Q）：你将得到整数l_i和r_i（1 ≦ l_i < r_i ≦ N）。考虑从索引l_i开始到索引r_i结束的S的子串（两者都包括在内）。在这个字符串中，AC作为一个子串出现了多少次？
#
#注释
#字符串T的子串是指从T的开头和结尾去除零个或多个字符后得到的字符串。
#例如，ATCODER的子串包括TCO、AT、CODER、ATCODER和（空字符串），但不包括AC。
#
#限制条件
#2 ≦ N ≦ 10^5
#1 ≦ Q ≦ 10^5
#S是一个长度为N的字符串。
#S中的每个字符都是A、C、G或T。
#1 ≦ l_i < r_i ≦ N
#
#输入
#输入是由标准输入法提供的，其格式如下：
#N Q
#S
#l_1 r_1
#:
#l_Q r_Q
#
#输出
#打印Q行。第i行应该包含第i个查询的答案。
#
#输入样本 1
#8 3
#ACACTACG
#3 7
#2 3
#1 8
#
#样本输出1
#2
#0
#3
#查询1：从索引3开始到索引7结束的S的子串是ACTAC。在这个字符串中，AC作为一个子串出现了两次。
#查询2：从索引2开始到索引3结束的S的子串是CA。在这个字符串中，AC作为一个子串出现了0次。
#查询3：从索引1开始到索引8结束的S的子串是ACACTACG。在这个字符串中，AC作为一个子串出现了三次。

def 