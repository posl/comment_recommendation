def main():
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    for i in range(n):
        if a[i] == i+1:
            cnt += 1
        else:
            continue
    print(cnt)
main()
