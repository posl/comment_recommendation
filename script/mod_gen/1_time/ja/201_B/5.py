def main():
    N = int(input())
    d = {}
    for i in range(N):
        S, T = input().split()
        d[S] = int(T)
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(d[1][0])

if __name__ == '__main__':
    main()