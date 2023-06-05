def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i-1 for i in a]
    cnt = 1
    i = x
    while a[i] != x:
        cnt += 1
        i = a[i]
    print(cnt)
main()
