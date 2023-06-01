Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            count += 1
    print(count)

=======
Suggestion 2

def count_odd_digits(n):
    count = 0
    for i in range(1, n+1):
        if i < 10:
            if i % 2 != 0:
                count += 1
        else:
            if i % 2 != 0:
                count += 1
            else:
                if i % 10 != 0:
                    if i % 100 != 0:
                        if i % 1000 != 0:
                            if i % 10000 != 0:
                                if i % 100000 != 0:
                                    if i % 1000000 != 0:
                                        if i % 10000000 != 0:
                                            if i % 100000000 != 0:
                                                if i % 1000000000 != 0:
                                                    count += 1
    return count

=======
Suggestion 3

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 1:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    odd = 0
    for i in range(1,n+1):
        if i % 2 == 1:
            odd += 1
    print(odd)

=======
Suggestion 5

def main():
    # 读取输入
    n = int(input())
    # 问题求解
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            count += 1
    # 输出结果
    print(count)

=======
Suggestion 6

def count_odd_digits(n):
    count = 0
    for i in range(1, n + 1):
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
    return count

n = int(input())
print(count_odd_digits(n))

=======
Suggestion 7

def odd_number(n):
    count = 0
    for i in range(1,n+1):
        if i < 10:
            if i % 2 == 1:
                count += 1
        elif i < 100:
            if i % 2 == 1:
                count += 1
        elif i < 1000:
            if i % 2 == 1:
                count += 2
        elif i < 10000:
            if i % 2 == 1:
                count += 2
        elif i < 100000:
            if i % 2 == 1:
                count += 3
        elif i < 1000000:
            if i % 2 == 1:
                count += 3
        elif i < 10000000:
            if i % 2 == 1:
                count += 4
        elif i < 100000000:
            if i % 2 == 1:
                count += 4
        elif i < 1000000000:
            if i % 2 == 1:
                count += 5
        elif i < 10000000000:
            if i % 2 == 1:
                count += 5

    return count
