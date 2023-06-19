Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i + j) % 2 == 0:
                        print("#", end="")
                    else:
                        print(".", end="")
                print("", end="")
            print("")
        print("")

=======
Suggestion 3

def main():
    n, a, b = map(int, input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i + j) % 2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print('', end='')
            print('')
        print('')

=======
Suggestion 4

def main():
    while True:
        try:
            line = input()
            if line == '':
                break
            line = line.split(' ')
            N = int(line[0])
            A = int(line[1])
            B = int(line[2])
            for i in range(N):
                for j in range(A):
                    for k in range(N):
                        for l in range(B):
                            if (i+j)%2 == 0:
                                print('.',end='')
                            else:
                                print('#',end='')
                    print()
        except:
            break

=======
Suggestion 5

def main():
    n,a,b = map(int,input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i + j) % 2 == 0:
                        print(".",end="")
                    else:
                        print("#",end="")
                print("")
        print("")

=======
Suggestion 6

def problems250_b(n,a,b):
    s = ''
    for i in range(n):
        for j in range(a):
            if i%2==0:
                s += '.'*b
            else:
                s += '#'*b
            s += '\n'
    print(s)

problems250_b(4,3,2)
problems250_b(5,1,5)
problems250_b(4,4,1)
problems250_b(1,4,4)

=======
Suggestion 7

def print_tile(a,b):
    for i in range(a):
        for j in range(b):
            if (i+j)%2==0:
                print('.',end='')
            else:
                print('#',end='')
        print()

=======
Suggestion 8

def main():
    n, a, b = map(int, input().split())
    for i in range(a*n):
        if i % 2 == 0:
            print('.' * (b*n))
        else:
            print('#' * (b*n))

=======
Suggestion 9

def main():
    # 读取输入
    N, A, B = map(int, input().split())
    # 构造输出
    for i in range(N * A):
        if i % A == 0:
            line = ''
        for j in range(N * B):
            if j % B == 0:
                line += '.'
            elif i % A == 0:
                line += '#'
            else:
                line += '.'
        print(line)

=======
Suggestion 10

def main():
    n,a,b = map(int,input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i + k) % 2 == 0:
                        print("#",end="")
                    else:
                        print(".",end="")
                print("")
        print("")
