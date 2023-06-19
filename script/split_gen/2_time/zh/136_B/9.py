def main():
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        if i < 10:
            cnt += 1
        elif i < 100:
            cnt += 1
        elif i < 1000:
            cnt += 1
        elif i < 10000:
            cnt += 1
        elif i < 100000:
            cnt += 1
    print(cnt)
main()
