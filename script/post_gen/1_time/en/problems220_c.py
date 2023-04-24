Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    #print("N:", N)
    #print("A:", A)
    #print("X:", X)
    sumA = sum(A)
    #print("sumA:", sumA)
    if sumA > X:
        #print("sumA > X")
        k = 0
        for i in range(N):
            if k > X:
                break
            k += A[i]
            #print("i:", i)
            #print("k:", k)
        print(i+1)
    else:
        #print("sumA <= X")
        k = 0
        for i in range(N):
            if k > X:
                break
            k += A[i]
            #print("i:", i)
            #print("k:", k)
        #print("i:", i)
        #print("k:", k)
        #print("i+1:", i+1)
        #print("N:", N)
        #print("(i+1)*N:", (i+1)*N)
        #print("k:", k)
        #print("sumA:", sumA)
        k = k + ((X-k)//sumA)*sumA
        #print("k:", k)
        for i in range(N):
            if k > X:
                break
            k += A[i]
            #print("i:", i)
            #print("k:", k)
        print((i+1)+(i+1)*N)
    return

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    S = sum(A)
    T = 0
    for i in range(N):
        T += A[i]
        if T > X:
            print(i+1)
            return
    if S <= 0:
        print(-1)
        return
    K = (X - T) // S
    T += K * S
    for i in range(N):
        T += A[i]
        if T > X:
            print(K * N + i + 1)
            return

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 10**5
    ans = 0
    sum = 0
    for i in range(len(B)):
        sum += B[i]
        ans += 1
        if sum > X:
            break
    print(ans)

=======
Suggestion 4

def solve(N, A, X):
    B = A * 100000
    sum = 0
    for i in range(1000000):
        sum += B[i]
        if sum > X:
            return i + 1
    return 0

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 100000
    #print(B)
    sum = 0
    for i in range(1000000):
        sum += B[i]
        if sum > X:
            print(i+1)
            break

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 100
    sumB = sum(B)
    if sumB > X:
        k = 0
        sumBk = 0
        while sumBk <= X:
            sumBk += B[k]
            k += 1
        print(k)
    else:
        k = 0
        sumBk = 0
        while sumBk <= X:
            sumBk += B[k]
            k += 1
        print(k + (X - sumBk) // sumB * N)

main()

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    
    sum_a = sum(a)
    sum_a100 = sum_a * 100
    
    if sum_a100 < x:
        print(-1)
        return
    
    k = 0
    s = 0
    for i in range(100):
        for j in range(n):
            s += a[j]
            k += 1
            if s > x:
                print(k)
                return

=======
Suggestion 8

def solve(N,A,X):
    B = A*100
    sum = 0
    for i in range(1000):
        sum += B[i]
        if sum > X:
            return i+1

N = int(input())
A = list(map(int,input().split()))
X = int(input())
print(solve(N,A,X))

=======
Suggestion 9

def solve(N, A, X):
    if sum(A) >= X:
        return 0
    B = A * 100
    k = 0
    s = 0
    while s < X:
        s += B[k]
        k += 1
    return k
