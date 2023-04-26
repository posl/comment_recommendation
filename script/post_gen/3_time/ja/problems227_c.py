Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for a in range(1, int(N**0.5)+1):
        for b in range(a, int(N**0.5)+1):
            for c in range(b, int(N**0.5)+1):
                if a*b*c <= N:
                    ans += 1
                else:
                    break
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for a in range(1, N+1):
        for b in range(a, N//a+1):
            c = N//a//b
            if a*b*c <= N:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for a in range(1, N+1):
        for b in range(1, N//a+1):
            c = N//a//b
            if a <= b <= c:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for a in range(1, N+1):
        for b in range(1, N//a+1):
            ans += N//(a*b)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for a in range(1, N+1):
        for b in range(a, N+1):
            if a*b > N:
                break
            ans += N//(a*b)
    print(ans)

main()

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for a in range(1,N+1):
        for b in range(a,N//a+1):
            ans += N//(a*b)
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for a in range(1, int(N**0.5)+1):
        for b in range(a, int(N/a**2)+1):
            c = N // (a*b)
            if c >= b:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N//i+1):
            ans += N//(i*j)
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    cnt = 0
    for c in range(1, N+1):
        cnt += (N//c)*(c-1)
        cnt += (N%c)
    print(cnt)
