def solve():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, 1 << N):
        bit = bin(i)[2:].zfill(N)
        pair = []
        for j in range(N):
            if bit[j] == '1':
                pair.append(j)
        if len(pair) == 2:
            ans = max(ans, A[pair[0]][pair[1]])
        elif len(pair) > 2:
            for j in range(len(pair)):
                for k in range(j + 1, len(pair)):
                    ans = max(ans, A[pair[j]][pair[k]])
    print(ans)
