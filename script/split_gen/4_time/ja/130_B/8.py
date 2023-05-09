def main():
    N, X = map(int, input().split())
    L_list = list(map(int, input().split()))
    cnt = 1
    D = 0
    for i in range(N):
        D = D + L_list[i]
        if D <= X:
            cnt = cnt + 1
    print(cnt)
