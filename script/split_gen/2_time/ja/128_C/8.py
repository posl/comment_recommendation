def main():
    N, M = map(int, input().split())
    switch = []
    for _ in range(M):
        switch.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        on = [0] * N
        for j in range(N):
            if ((i >> j) & 1):
                on[j] = 1
        flag = True
        for j in range(M):
            count = 0
            for k in range(1, switch[j][0]+1):
                if on[switch[j][k]-1] == 1:
                    count += 1
            if count % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
