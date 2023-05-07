def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x:x[0])
    pos = 0
    for i in range(N):
        if K >= AB[i][0] - pos:
            K += AB[i][1] - (AB[i][0] - pos)
            pos = AB[i][0]
        else:
            pos += K
            K = 0
            break
    pos += K
    print(pos)
