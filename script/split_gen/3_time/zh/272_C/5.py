def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max_even = -1
    for i in range(N):
        if A[i] % 2 == 0:
            max_even = A[i]
    if max_even == -1:
        print(-1)
    else:
        for i in range(N):
            for j in range(i+1, N):
                if A[i] + A[j] == max_even:
                    print(max_even)
                    return
        print(-1)
        return
