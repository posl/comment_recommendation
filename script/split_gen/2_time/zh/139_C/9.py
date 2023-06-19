def main():
    N = int(input())
    H = list(map(int, input().split()))
    # print(N)
    # print(H)
    ans = 0
    count = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
        else:
            ans = max(ans, count)
            count = 0
    ans = max(ans, count)
    print(ans)
