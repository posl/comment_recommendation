def main():
    N = int(input())
    p = list(map(int, input().split()))
    p_sorted = sorted(p)
    count = 0
    for i in range(N):
        if p[i] != p_sorted[i]:
            count += 1
    if count == 2 or count == 0:
        print('YES')
    else:
        print('NO')
