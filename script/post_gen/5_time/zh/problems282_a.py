Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    print("".join(chr(65+i) for i in range(k)))

=======
Suggestion 2

def main():
    # 读取输入
    k = int(input())
    # 打印答案
    print(''.join([chr(ord('A')+i) for i in range(k)]))

=======
Suggestion 3

def main():
    K = int(input())
    print(''.join([chr(ord('A')+i) for i in range(K)]))

=======
Suggestion 4

def main():
    k = int(input())
    #print(chr(65))
    for i in range(k):
        print(chr(65+i), end='')

=======
Suggestion 5

def main():
    K = int(input())
    print(''.join([chr(i) for i in range(65, 65+K)]))

=======
Suggestion 6

def main():
    k = int(input())
    print(''.join([chr(ord('A')+i) for i in range(k)]))

=======
Suggestion 7

def main():
    k = int(input())
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(alp[:k])

=======
Suggestion 8

def main():
    k = int(input())
    print(''.join([chr(i) for i in range(65,65+k)]))
