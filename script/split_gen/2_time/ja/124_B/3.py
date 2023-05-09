def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 1
    for i in range(N-1):
        if H[i] <= H[i+1]:
            cnt += 1
    print(cnt)
