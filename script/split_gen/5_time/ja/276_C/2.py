def main():
    N = int(input())
    P = list(map(int,input().split()))
    n = 1
    for i in range(2,N+1):
        n *= i
    for i in range(n):
        if P != list(range(1,N+1)):
            P = P[1:] + [P[0]]
        else:
            break
    print(*P)
main()
