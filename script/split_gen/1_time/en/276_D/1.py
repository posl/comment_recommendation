def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            elif A[i] % 3 == 0:
                A[i] //= 3
            else:
                print(-1)
                return
        if len(set(A)) == 1:
            break
        count += 1
    print(count)
