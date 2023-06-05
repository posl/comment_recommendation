def main():
    c = input()
    print(chr(ord(c)+1))
main()
# Path: pre_gen/zh/problems152_a.py
#问题陈述
#给出的是一个小写英文字母C，它不是a，按字母顺序打印C前面的字母。
#
#限制条件
#C是一个小写的英文字母，不是a。
#
#输入
#输入是由标准输入法提供的，其格式如下：
#C
#
#输出
#按字母顺序打印C前面的字母。
#
#输入样本1
#b
#
#样本输出1
#a
#b前面是a。
#
#样本输入2
#z
#
#样本输出2
#y
#z前面是y。

if __name__ == '__main__':
    main()