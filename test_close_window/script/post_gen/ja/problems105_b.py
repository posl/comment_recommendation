Synthesizing 10/10 solutions

=======

def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 4 == 7 or N % 7 == 4:
        print("Yes")
    else:
        print("No")

=======

def main():
    n = int(input())
    for i in range(n//4+1):
        for j in range(n//7+1):
            if 4*i+7*j == n:
                print("Yes")
                return
    print("No")
    return

=======

def main():
    n = int(input())
    for i in range(n+1):
        for j in range(n+1):
            if 4*i + 7*j == n:
                print("Yes")
                return
    print("No")

=======

def main():
    N = int(input())
    if N%4 == 0 or N%7 == 0 or N%4%7 == 0 or N%7%4 == 0:
        print("Yes")
    else:
        print("No")

=======

def main():
    N = int(input())
    if N == 1 or N == 2 or N == 3 or N == 5 or N == 6 or N == 8 or N == 9 or N == 10:
        print('No')
    else:
        print('Yes')

=======

def main():
    N = int(input())
    ans = "No"
    for i in range(0,N+1):
        for j in range(0,N+1):
            if 4*i + 7*j == N:
                ans = "Yes"
                break
    print(ans)

=======

def main():
    N = int(input())
    ans = "No"
    for i in range(N//4 + 1):
        if (N - 4*i) % 7 == 0:
            ans = "Yes"
    print(ans)

=======

def main():
    N = int(input())
    for i in range(N+1):
        if i*4 + (N-i)*7 == N:
            print("Yes")
            exit()
    print("No")

=======

def main():
    n = int(input())
    if n >= 4:
        if n % 4 == 0:
            print("Yes")
        elif n % 7 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======

def main():
    # 入力
    N = int(input())
    # 処理
    for i in range(0,N+1):
        for j in range(0,N+1):
            if i*4 + j*7 == N:
                ans = "Yes"
                break
            else:
                ans = "No"
        if ans == "Yes":
            break
    # 出力
    print(ans)
