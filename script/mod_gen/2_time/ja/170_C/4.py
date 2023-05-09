def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        return
    p = list(map(int, input().split()))
    p.sort()
    #print(p)
    if X < p[0]:
        print(p[0])
        return
    elif X > p[-1]:
        print(p[-1])
        return
    else:
        for i in range(len(p)-1):
            if X > p[i] and X < p[i+1]:
                if X - p[i] > p[i+1] - X:
                    print(p[i+1])
                    return
                else:
                    print(p[i])
                    return

if __name__ == '__main__':
    main()