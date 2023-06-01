Synthesizing 10/10 solutions

=======
Suggestion 1

def add_comma(num):
    if num < 1000:
        return str(num)
    else:
        return add_comma(num//1000) + ',' + '{:03d}'.format(num%1000)

n = int(input())
print(len(add_comma(n).split(','))-1)

=======
Suggestion 2

def main():
    # 读取输入
    N = int(input().strip())

    # 初始化
    ans = 0
    # 逐位判断
    while N > 0:
        # 逢三进一
        ans += (N + 2) // 3
        # 去掉最后三位
        N //= 10

    # 输出结果
    print(ans)

=======
Suggestion 3

def get_comma_count(n):
    comma_count = 0
    for i in range(1, len(str(n))):
        if i % 3 == 0:
            comma_count += 1
    return comma_count

=======
Suggestion 4

def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    if N_len <= 3:
        print(0)
        return
    if N_len % 3 == 0:
        print((N_len//3-1)*2)
    else:
        print((N_len//3)*2)

=======
Suggestion 5

def count_comma(n):
    if n <= 999:
        return 0
    else:
        s = str(n)
        l = len(s)
        if l % 3 == 0:
            return (l // 3 - 1) * 2 + count_comma(int(s[3:]))
        else:
            return (l // 3) * 2 + count_comma(int(s[l % 3:]))

=======
Suggestion 6

def main():
    N = int(input())
    if N < 1000:
        print(0)
    elif N < 1000000:
        print(N-999)
    elif N < 1000000000:
        print(2*(N-999999)+999000)
    elif N < 1000000000000:
        print(3*(N-999999999)+1998000000)
    elif N < 1000000000000000:
        print(4*(N-999999999999)+2999700000000)
    else:
        print(5*(N-999999999999999)+3999960000000000)

=======
Suggestion 7

def count_comma(n):
    if n < 1000:
        return 0
    else:
        count = 0
        while n > 1000:
            count += 1
            n = n / 1000
        return count

=======
Suggestion 8

def main():
    n = int(input())
    count = 0
    for i in range(1, len(str(n))+1):
        if i % 3 == 0:
            count += 1
    print(count)

=======
Suggestion 9

def get_comma_num(num):
    result = 0
    num_list = [int(i) for i in str(num)]
    num_len = len(num_list)
    for i in range(1, num_len):
        if i % 3 == 0:
            result += 1
    return result

=======
Suggestion 10

def count_comma(n):
    result = 0
    if n >= 1000:
        result += 1
    if n >= 1000000:
        result += 1
    if n >= 1000000000:
        result += 1
    if n >= 1000000000000:
        result += 1
    if n >= 1000000000000000:
        result += 1
    return result
