def main():
    N, M = map(int, input().split())
    uv = [list(map(int, input().split())) for _ in range(M)]
    uv.sort()
    for i in range(M):
        uv[i].sort()
    uv.sort(key=lambda x: x[0])
    print(uv)
    for i in range(N):
        if uv[i][0] != i+1:
            print('No')
            exit()
    else:
        print('Yes')
