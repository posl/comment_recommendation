def main():
    N = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if p[i] == i:
            cnt += 1
    print(cnt // 2 + cnt % 2)
main()
