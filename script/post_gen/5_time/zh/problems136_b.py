Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n=int(input())
    count=0
    for i in range(1,n+1):
        if i<10:
            count+=1
        elif i<100:
            count+=1
        elif i<1000:
            count+=1
        elif i<10000:
            count+=1
        elif i<100000:
            count+=1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if i % 2 != 0:
            count += 1
    print(count)

=======
Suggestion 3

def count_odd(n):
    count = 0
    for i in range(1, n + 1):
        if i < 10:
            if i % 2 != 0:
                count += 1
        else:
            if i % 2 != 0:
                count += 1
            else:
                for j in range(1, len(str(i))):
                    if int(str(i)[j]) % 2 != 0:
                        count += 1
                        break
    return count

print(count_odd(100000))

=======
Suggestion 4

def main():
    # 读取输入
    N = int(input())

    # 计算并输出结果
    count = 0
    for i in range(1, N + 1):
        # 将数字转换成字符串，然后判断奇偶
        if str(i).count('1') % 2 == 1:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    count = 0
    for i in range(1,n+1):
        if i < 10:
            count += 1
        elif i < 100:
            count += 1
        elif i < 1000:
            count += 2
        elif i < 10000:
            count += 2
        elif i < 100000:
            count += 3
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 1:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def solution(N):
    count = 0
    for i in range(1,N+1):
        if i < 10:
            if i % 2 == 1:
                count += 1
        else:
            if i % 2 == 1:
                count += 1
            else:
                for j in range(1,len(str(i))):
                    if int(str(i)[j]) % 2 == 1:
                        count += 1
                        break
    return count

=======
Suggestion 8

def get_odd_num(n):
    if n < 10:
        return n
    else:
        odd_num = 9
        for i in range(10, n+1):
            if i % 2 == 1:
                odd_num += 1
        return odd_num

=======
Suggestion 9

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 1:
            ans += 1
    print(ans)

=======
Suggestion 10

def count_odd_digits(n):
    count = 0
    for i in range(1,n+1):
        if i < 10:
            if i % 2 == 1:
                count += 1
        elif i < 100:
            if i % 10 % 2 == 1:
                count += 1
            if i // 10 % 2 == 1:
                count += 1
        elif i < 1000:
            if i % 10 % 2 == 1:
                count += 1
            if i // 10 % 10 % 2 == 1:
                count += 1
            if i // 100 % 2 == 1:
                count += 1
        elif i < 10000:
            if i % 10 % 2 == 1:
                count += 1
            if i // 10 % 10 % 2 == 1:
                count += 1
            if i // 100 % 10 % 2 == 1:
                count += 1
            if i // 1000 % 2 == 1:
                count += 1
        elif i < 100000:
            if i % 10 % 2 == 1:
                count += 1
            if i // 10 % 10 % 2 == 1:
                count += 1
            if i // 100 % 10 % 2 == 1:
                count += 1
            if i // 1000 % 10 % 2 == 1:
                count += 1
            if i // 10000 % 2 == 1:
                count += 1
        else:
            if i % 10 % 2 == 1:
                count += 1
            if i // 10 % 10 % 2 == 1:
                count += 1
            if i // 100 % 10 % 2 == 1:
                count += 1
            if i // 1000 % 10 % 2 == 1:
                count += 1
            if i // 10000 % 10 % 2 == 1:
                count += 1
            if i // 100000 % 2 == 1:
                count += 1
    return count

n
