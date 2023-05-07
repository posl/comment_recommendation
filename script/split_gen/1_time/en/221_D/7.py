def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #A.append(0)
    #B.append(0)
    #N += 1
    #A, B = zip(*sorted(zip(A, B), key=lambda x: x[0]))
    #print(A)
    #print(B)
    #print(N)
    day = [0] * (10**9+2)
    for i in range(N):
        day[A[i]] += 1
        day[A[i]+B[i]] -= 1
    #print(day)
    for i in range(1, 10**9+2):
        day[i] += day[i-1]
    #print(day)
    day = day[1:-1]
    #print(day)
    day = sorted(day)
    #print(day)
    for i in range(N):
        print(day[i], end=" ")
    print()
