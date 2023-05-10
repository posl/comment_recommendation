def main():
    N = int(input())
    ab = [list(map(int, input().split())) for _ in range(N)]
    ab.sort(key=lambda x: x[0] + x[0] + x[1], reverse=True)
    aoki = sum([x[0] for x in ab])
    takahashi = 0
    for i in range(N):
        aoki -= ab[i][0]
        takahashi += ab[i][0] + ab[i][1]
        if aoki < takahashi:
            print(i + 1)
            exit()
