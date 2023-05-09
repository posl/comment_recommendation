def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(N):
        if a[N-i-1] == 1:
            b.append(N-i)
            for j in range(N-i-1, N, N-i-1):
                a[j] = 1 - a[j]
    print(len(b))
    print(' '.join(map(str, b)))
