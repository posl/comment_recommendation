def main():
    N = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if p[i] != i+1:
            cnt += 1
    print('YES' if cnt <= 2 else 'NO')
