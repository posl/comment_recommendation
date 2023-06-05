Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    K = int(input())
    print(''.join([chr(i) for i in range(ord('A'), ord('A')+K)]))

=======
Suggestion 2

def main():
    # 读取数据
    k = int(input())
    # 处理数据
    # 输出结果
    print("".join([chr(ord('A')+i) for i in range(k)]))

=======
Suggestion 3

def main():
    k = int(input())
    print(''.join([chr(ord('A') + i) for i in range(k)]))

=======
Suggestion 4

def main():
    k = int(input())
    print(''.join(chr(ord('A') + i) for i in range(k)))

=======
Suggestion 5

def main():
    K = int(input())
    for i in range(K):
        print(chr(i+65),end='')

=======
Suggestion 6

def main():
    k = int(input())
    for i in range(k):
        print(chr(ord('A')+i),end='')
    print()

=======
Suggestion 7

def main():
    k = int(input())
    print(''.join([chr(i) for i in range(ord('A'), ord('A')+k)]))

=======
Suggestion 8

def main():
    K = int(input())
    print("".join([chr(i) for i in range(65, 65 + K)]))

=======
Suggestion 9

def main():
    k = int(input())
    s = ''
    for i in range(k):
        s += chr(i + ord('A'))
    print(s)

=======
Suggestion 10

def main():
    K = int(input())
    s = ''
    for i in range(K):
        s += chr(ord('A') + i)
    print(s)

main()
