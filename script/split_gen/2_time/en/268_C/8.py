def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if (i + 1) == p[i]:
            if i == 0:
                if p[N - 1] == N - 1:
                    count += 1
            else:
                if p[i - 1] == i - 1:
                    count += 1
    print(count)
