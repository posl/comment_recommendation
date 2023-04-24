Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    for i in range(N//4 + 1):
        for j in range(N//7 + 1):
            if 4*i + 7*j == N:
                print("Yes")
                return
    print("No")

=======
Suggestion 2

def main():
    N = int(input())
    for i in range(N+1):
        for j in range(N+1):
            if 4*i + 7*j == N:
                print("Yes")
                return
    print("No")

=======
Suggestion 3

def main():
    N = int(input())
    for i in range(N+1):
        for j in range(N+1):
            if i*4 + j*7 == N:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 4

def main():
    N = int(input())
    ans = "No"
    for i in range(N//4+1):
        for j in range(N//7+1):
            if 4*i+7*j == N:
                ans = "Yes"
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    flag = False
    for i in range(N//4+1):
        for j in range(N//7+1):
            if 4*i + 7*j == N:
                flag = True
                break
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N = int(input())
    if N == 1 or N == 2 or N == 3 or N == 5 or N == 6:
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def main():
    N = int(input())
    for i in range(N+1):
        for j in range(N+1):
            if 4*i+7*j == N:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 8

def main():
    N = int(input())
    print("Yes" if N % 4 == 0 or N % 7 == 0 or N % 4 == 7 or N % 7 == 4 else "No")

=======
Suggestion 9

def main():
    N = int(input())
    for i in range(N//4+1):
        if (N-4*i)%7 == 0:
            print("Yes")
            break
    else:
        print("No")

=======
Suggestion 10

def main():
    N = int(input())
    cake = 4
    donuts = 7
    for i in range(N//cake+1):
        for j in range(N//donuts+1):
            if i*cake + j*donuts == N:
                print("Yes")
                return
    print("No")
