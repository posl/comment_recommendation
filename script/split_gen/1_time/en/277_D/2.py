def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    count = [0] * M
    for a in A:
        count[a] += 1
    if count[0] == N:
        print(0)
        return
    if count[0] % 2 == 1:
        count[0] = 1
    else:
        count[0] = 0
    for i in range(1, M):
        if count[i] == 0:
            continue
        if count[i] % 2 == 1:
            count[i] = 1
        else:
            count[i] = 0
    count = count[::-1]
    print(N - count.index(1))
main()
