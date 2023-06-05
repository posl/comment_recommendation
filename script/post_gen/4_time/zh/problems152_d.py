Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        a = str(i)
        b = a[::-1]
        if a[0] == b[-1] and a[-1] == b[0]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    if N<10:
        print(N)
    elif N<100:
        print(9)
    elif N<1000:
        print(9+((N-99)//10))
    elif N<10000:
        print(9+90+((N-999)//100))
    elif N<100000:
        print(9+90+900+((N-9999)//1000))
    elif N<1000000:
        print(9+90+900+9000+((N-99999)//10000))
    elif N<10000000:
        print(9+90+900+9000+90000+((N-999999)//100000))
    elif N<100000000:
        print(9+90+900+9000+90000+900000+((N-9999999)//1000000))
    elif N<1000000000:
        print(9+90+900+9000+90000+900000+9000000+((N-99999999)//10000000))
    elif N<10000000000:
        print(9+90+900+9000+90000+900000+9000000+90000000+((N-999999999)//100000000))
    elif N<100000000000:
        print(9+90+900+9000+90000+900000+9000000+90000000+900000000+((N-9999999999)//1000000000))
    elif N<1000000000000:
        print(9+90+900+9000+90000+900000+9000000+90000000+900000000+9000000000+((N-99999999999)//10000000000))
    elif N<10000000000000:
        print(9+90+900+9000+90000+900000+9000000+90000000+900000000+9000000000+90000000000+((N-999999999999)//100000000000))
    elif N<100000000000000:
        print(9+90+900+9000+90000+900000+9000000+90000000+900000000+9000000000+900000

=======
Suggestion 3

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i % 10 == j // (10 ** (len(str(j))-1)) and i // (10 ** (len(str(i))-1)) == j % 10:
                count += 1
    print(count)

=======
Suggestion 4

def is_ok(n):
    s = str(n)
    if len(s) == 1:
        return True
    else:
        if s[0] == s[-1]:
            return True
        else:
            return False

=======
Suggestion 5

def main():
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        if i % 10 == 0:
            continue
        for j in range(1, n + 1):
            if j % 10 == 0:
                continue
            if str(i)[0] == str(j)[-1] and str(i)[-1] == str(j)[0]:
                count += 1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if int(str(i)[-1]) == int(str(j)[0]) and int(str(i)[0]) == int(str(j)[-1]):
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        str_i = str(i)
        if str_i[0] == str_i[-1]:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    # 读入
    N = int(input())
    # 初始化
    ans = 0
    # 遍历
    for i in range(1, N + 1):
        # 求一下最后一位
        last = i % 10
        # 如果最后一位是0，那么就跳过
        if last == 0:
            continue
        # 求一下第一位
        first = int(str(i)[0])
        # 如果第一位也是0，那么也跳过
        if first == 0:
            continue
        # 如果满足条件，那么就加一
        if last == first:
            ans += 1
    # 打印
    print(ans)
main()

=======
Suggestion 9

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i % 10 == 0:
            continue
        else:
            str_i = str(i)
            if str_i[0] == str_i[-1]:
                ans += 1
            for j in range(i+1, N+1):
                str_j = str(j)
                if str_i[-1] == str_j[0] and str_j[-1] == str_i[0]:
                    ans += 2
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if int(str(i)[-1]) == int(str(j)[0]) and int(str(i)[0]) == int(str(j)[-1]):
                cnt += 1
    print(cnt)
