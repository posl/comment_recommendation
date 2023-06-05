def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    tmp = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            tmp += 1
        else:
            if tmp > ans:
                ans = tmp
            tmp = 0
    print(ans)
