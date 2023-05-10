def main():
    N,X = map(int,input().split())
    AB = [list(map(int,input().split())) for i in range(N)]
    AB.sort(key=lambda x: x[1],reverse=True)
    t = 0
    for i in range(N):
        t += AB[i][0] + AB[i][1]
        if t > X:
            print(t - AB[i][1])
            exit()
    print(t)

if __name__ == '__main__':
    main()