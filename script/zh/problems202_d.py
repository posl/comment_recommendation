#问题陈述
#在长度为A+B的字符串中，包含A的出现次数和B的出现次数的字符串中，找出按词典顺序排列的第K个字符串。
#
#限制条件
#1 ≦ A, B ≦ 30
#1 ≦ K ≦ S，其中S是长度为A+B的字符串的数量，包含A出现的a和B出现的b。
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#A B K
#
#輸出
#打印答案。
#
#输入样本 1
#2 2 4
#
#输出样本 1
#baab
#下面是包含两个as和两个b的字符串，按词典顺序排列：aabb, abab, abba, baab, baba, and bbaa。
#第四个字符串，baab，应该被打印出来。
#
#输入样本 2
#30 30 118264581564861424
#
#输出样本2
#bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
#K可能不适合32位整数类型。

def 