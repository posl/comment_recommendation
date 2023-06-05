def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if h[i] >= max(h[:i+1]):
            cnt += 1
    print(cnt)
main()
