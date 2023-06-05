def main():
    n,m,t = map(int, input().split())
    ab = []
    for i in range(m):
        a,b = map(int, input().split())
        ab.append((a,b))
    ab.sort()
    bat = n
    time = 0
    for i in range(m):
        bat -= ab[i][0] - time
        if bat <= 0:
            print("No")
            exit()
        bat += ab[i][1] - ab[i][0]
        bat = min(bat, n)
        time = ab[i][1]
    bat -= t - time
    if bat <= 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()