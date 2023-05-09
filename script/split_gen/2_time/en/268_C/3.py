def main():
    N = int(input())
    p = list(map(lambda x: int(x) - 1, input().split()))
    count = 0
    for i in range(N):
        if p[i] == i:
            count += 1
    if count == N:
        print(N)
    else:
        print(N - count + 2 * (count % 2))
