def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        flag = True
        for j in range(N):
            if S[j] == 'AND':
                if i & (1 << j) == 0:
                    flag = False
                    break
            else:
                if i & (1 << j) != 0:
                    flag = False
                    break
        if flag:
            ans += 1
    print(ans)
