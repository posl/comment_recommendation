#问题说明
#AtCoder Grand Contest（AGC）是一个定期举行的具有世界权威性的比赛，已经举行了54次。
#就像第230届ABC--也就是你现在所在的那届--被称为ABC230一样，第N届AGC最初是用一个零填充的3位数N来命名的（第1届AGC为AGC001，第2届AGC为AGC002，...）。
#然而，最新的第54个AGC被称为AGC055，其中数字是比54大的一个。因为AGC042由于社会情况而被取消和缺失，所以第42次和以后的比赛被分配的号码比所举行的比赛的数量大一。(参见样本输入和输出的解释)。
#问题是：给定一个整数N，以AGCXXX的格式打印第N个AGC的名称，其中XXX是加零的3位数字。
#
#限制条件
#1 ≦ N ≦ 54
#N是一个整数。
#
#输入
#输入由标准输入提供，格式如下：
#N
#
#输出
#以指定格式打印第N个AGC的名称。
#
#样本输入1
#42
#
#样本输出1
#AGC043
#正如问题陈述中所解释的，第42个及以后的AGC被分配的数字比比赛的数字大一。
#因此，第42个AGC被命名为AGC043。
#
#样本输入2
#19
#
#采样输出2
#AGC019
#第41个和前面的AGC被分配的数字与比赛的数字相等。
#因此，答案是AGC019。
#
#样本输入3
#1
#
#样本输出3
#AGC001
#如问题陈述中所述，第1个AGC被命名为AGC001。
#请确保用零来填充这个数字，使之成为一个3位数的数字。
#
#输入样本4
#50
#
#采样输出4
#AGC051

def 