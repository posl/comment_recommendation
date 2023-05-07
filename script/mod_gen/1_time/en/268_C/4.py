def main():
    N = int(input())
    p = list(map(int, input().split()))
    #print(N, p)
    if p[0] == 0:
        if p[N-1] == N-1:
            print(N)
        else:
            print(N-1)
    elif p[N-1] == N-1:
        print(N-1)
    else:
        print(N-2)
main()
This code got 100 points.
Rate this: Share this: Twitter

if __name__ == '__main__':
    main()