#问题陈述
#高桥想成为某个网络服务的成员。
#他试图用ID S来注册，结果发现这个ID已经被另一个用户使用了。
#因此，他决定用一个字符串作为他的ID，这个字符串是在S的末尾加上一个字符得到的。
#他现在试图用ID T进行注册。请判断这个字符串是否满足上述属性。
#
#限制条件
#S和T是由小写英文字母组成的字符串。
#1 ≦ |S| ≦ 10
#|T| = |S| + 1
#
#输入
#输入是由标准输入法提供的，其格式如下：
#S
#T
#
#輸出
#如果T满足问题陈述中的属性，打印Yes；否则，打印No。
#
#输入样本1
#chokudai
#丘克达伊兹
#
#样本输出1
#是
#chokudaiz可以通过在chokudai的末尾加上z来获得。
#
#输入样本2
#snuke
#snekee
#
#样本输出2
#没有
#snekee不能通过在snuke的末尾添加一个字符来获得。
#
#输入样本3
#a
#aa
#
#样品输出3
#是

def 