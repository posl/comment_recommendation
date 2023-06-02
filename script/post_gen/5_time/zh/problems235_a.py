Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(a+b+c)

=======
Suggestion 2

def main():
    abc = int(input())
    bca = abc % 10 * 100 + abc // 10 % 10 * 10 + abc // 100
    cab = abc // 100 * 100 + abc % 10 * 10 + abc // 10 % 10
    print(abc + bca + cab)

=======
Suggestion 3

def main():
    # 读取输入
    abc = input()
    # 计算abc+bca+cab
    bca = int(abc[1]+abc[2]+abc[0])
    cab = int(abc[2]+abc[0]+abc[1])
    sum = int(abc)+bca+cab
    # 输出结果
    print(sum)

main()

=======
Suggestion 4

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a * 111 + b * 111 + c * 111)

=======
Suggestion 5

def problems235_a():
    abc = int(input())
    bca = abc//100*100 + abc%100//10*10 + abc%10
    cab = abc%10*100 + abc%100//10*10 + abc//100
    print(abc+bca+cab)

=======
Suggestion 6

def problem235_a():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a*111+b*11+c*1+b*100+c*10+a*1+c*100+a*10+b*1)

problem235_a()

=======
Suggestion 7

def main():
    abc = input()
    abc = int(abc)
    a = abc // 100
    b = abc // 10 % 10
    c = abc % 10
    print(a * 100 + b * 10 + c + b * 100 + c * 10 + a + c * 100 + a * 10 + b)

=======
Suggestion 8

def get_number():
    num = int(input())
    return num

=======
Suggestion 9

def main():
    abc = int(input())
    a = abc // 100
    b = (abc // 10) % 10
    c = abc % 10
    print(abc + 100 * b + 10 * c + 100 * c + 10 * a + b + 100 * a + 10 * c + b)
