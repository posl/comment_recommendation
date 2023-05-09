def solve():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab = sorted(ab, key=lambda x: x[0]+x[1])
    print(ab[-1][0]+ab[-1][1])
