def main():
    N, S = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, 1 << N):
        sum = 0
        ans = []
        for j in range(N):
            if i & (1 << j):
                sum += AB[j][0]
                ans.append('T')
            else:
                sum += AB[j][1]
                ans.append('H')
        if sum == S:
            print('Yes')
            print(''.join(ans))
            return
    print('No')
