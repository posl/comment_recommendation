Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    t = 0
    for i in range(n):
        t += a[i] / b[i]
    t /= 2
    s = 0
    for i in range(n):
        s += a[i] / b[i]
        if s >= t:
            print(a[i] - (s - t) * b[i])
            break

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a_sum = sum(a)
    b_sum = sum(b)
    print(a_sum * 1.0 / b_sum)

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        ans += A[i]/B[i]
    ans = ans*2/N
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    left = 0
    right = 0
    for i in range(N):
        left += A[i]/B[i]
        right += A[N-i-1]/B[N-i-1]
    if left == right:
        print(left)
    else:
        left = 0
        right = 0
        for i in range(N):
            left += A[i]/B[i]
            right += A[N-i-1]/B[N-i-1]
            if left == right:
                print(left)
                break
            elif left > right:
                for j in range(i+1,N):
                    left += A[j]/B[j]
                    right += A[N-j-1]/B[N-j-1]
                    if left == right:
                        print(left)
                        break
                    elif left > right:
                        continue
                    else:
                        print(left)
                        break
            else:
                for j in range(i+1,N):
                    left += A[j]/B[j]
                    right += A[N-j-1]/B[N-j-1]
                    if left == right:
                        print(left)
                        break
                    elif left > right:
                        print(right)
                        break
                    else:
                        continue
        else:
            print(left)

main()

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    left = 0
    right = 0
    for i in range(N):
        left += A[i] / B[i]
        right += A[N - 1 - i] / B[N - 1 - i]

    if left == right:
        print(left)
    elif left > right:
        left = 0
        for i in range(N):
            left += A[i] / B[i]
            if left >= right:
                print(left)
                break
    else:
        right = 0
        for i in range(N):
            right += A[N - 1 - i] / B[N - 1 - i]
            if right >= left:
                print(right)
                break

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    sum_A = sum(A)
    sum_B = sum(B)
    ans = sum_A/sum_B
    print(ans)
main()

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    res = 0
    for i in range(N):
        res += A[i]/B[i]
    res = res*2/N
    print(res)

=======
Suggestion 8

def main():
    n = int(input())
    A = []
    B = []
    for _ in range(n):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(n):
        ans += A[i]/B[i]
    ans /= 2
    for i in range(n):
        ans -= A[i]/B[i]
        if ans <= 0:
            ans += A[i]/B[i]
            break
    ans *= B[i]
    print(ans)

=======
Suggestion 9

def get_input(): 
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    return N, A, B

=======
Suggestion 10

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #init
    t = 0
    l = 0
    r = 0
    for i in range(N):
        t += A[i]/B[i]
        l += A[i]
        r += A[i]/B[i]

    #binary search
    while r-l > 10**(-6):
        m = (l+r)/2
        if m < t/2:
            l = m
        else:
            r = m

    #calc
    ans = 0
    for i in range(N):
        if r > A[i]/B[i]:
            ans += A[i]/B[i]**2
            r -= A[i]/B[i]
        else:
            ans += r**2/B[i]
            break

    print(ans)
