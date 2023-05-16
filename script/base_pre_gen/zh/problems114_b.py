#问题陈述
#有一个由数字1，2，...，9组成的字符串S。
#腊肠犬Lunlun会从S中取出三个连续的数字，把它们当作一个单一的整数X，并把它带给它的主人。(她不能重新排列这些数字）。
#主人最喜欢的数字是753。越接近这个数字就越好。
#X和753之间的最小可能（绝对）差异是多少？
#
#限制条件
#S是一个长度在4到10（包括10）之间的字符串。
#S中的每个字符是1，2，...，或9。
#
#输入
#输入是由标准输入法提供的，其格式如下：
#S
#
#输出
#打印X和753之间的最小可能差异。
#
#输入样本1
#1234567876
#
#样本输出1
#34
#去掉第七至第九个字符的结果是X=787，与753的差值是787-753=34。无论从哪里取出X，这个差值都不会变小。
#请注意，这些数字不能重新排列。例如，取出567并重新排列成765是不允许的。
#我们也不能从S中取出不连续的三个数字。例如，不允许拿出第七位数字7，第九位数字7和第十位数字6来得到776。
#
#输入样本2
#35753
#
#样本输出2
#0
#如果753本身可以取出来，答案是0。
#
#样本输入3
#1111111111
#
#样本输出3
#642
#不管X从哪里来，X=111，差值为753-111=642。

def 