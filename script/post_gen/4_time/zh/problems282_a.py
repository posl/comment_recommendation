Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    print(''.join([chr(i) for i in range(ord('A'), ord('A') + k)]))

=======
Suggestion 2

def main():
    K = int(input())
    for i in range(K):
        print(chr(ord('A') + i), end='')
    print()

=======
Suggestion 3

def main():
    k = int(input())
    print(''.join([chr(ord('A') + i) for i in range(k)]))

=======
Suggestion 4

def main():
    k = int(input())
    print("".join([chr(i) for i in range(ord('A'), ord('A') + k)]))

=======
Suggestion 5

def main():
    # 读入数据
    k = int(input())

    # 处理数据
    ans = ""
    for i in range(k):
        ans += chr(ord('A') + i)

    # 输出结果
    print(ans)

=======
Suggestion 6

def main():
    k = int(input())
    s = ''
    for i in range(k):
        s += chr(ord('A')+i)
    print(s)

=======
Suggestion 7

def main():
    K = int(input())
    print(''.join([chr(ord('A') + i) for i in range(K)]))

=======
Suggestion 8

def main():
    K = int(input())
    print("".join([chr(i) for i in range(ord('A'), ord('A')+K)]))

=======
Suggestion 9

def main():
    k = int(input())
    for i in range(k):
        print(chr(65+i),end="")
    print()

=======
Suggestion 10

def main():
    k = int(input())
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(s[:k])
