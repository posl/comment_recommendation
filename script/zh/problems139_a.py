#问题陈述
#你将得到一个长度为3的字符串S，代表过去三天的天气预报。
#S的第i个字符（1 ≦ i ≦ 3）代表第i天的预报。S、C和R分别代表晴天、阴天和雨天。
#你还将得到一个长度为3的字符串T，代表这三天的实际天气。
#S的第i个字符（1 ≦ i ≦ 3）代表第i天的实际天气。S、C和R分别代表晴天、阴天和雨天。
#打印预测正确的天数。
#
#限制条件
#S和T是每个长度为3的字符串。
#S和T由S、C和R组成。
#
#输入
#输入由标准输入提供，格式如下：
#S
#T
#
#输出
#打印预测正确的天数。
#
#输入样本1
#CSS
#CSR
#
#样本输出1
#2
#第一天，天气预报说是多云的，而且确实是多云的。
#第二天，天气预报说是晴天，确实是晴天。
#第三天，天气预报是晴天，但却下雨了。
#因此，在这种情况下，有两天的预报是正确的。
#
#样本输入2
#卫星数据（SSR
#SSR
#
#采样输出2
#3
#
#采样输入3
#RRR
#SSS
#
#采样输出3
#0

def 