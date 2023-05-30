def main():
    n,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort()
    now = k
    for i in range(n):
        if now >= ab[i][0]:
            now += ab[i][1]
        else:
            print(now)
            exit()
    print(now)
main()
