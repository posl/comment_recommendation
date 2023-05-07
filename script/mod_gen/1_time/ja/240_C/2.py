def main():
    N, X = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    #print(N, X)
    #print(a)
    #print(b)
    for i in range(N):
        if X >= a[i] and X <= b[i]:
            print("Yes")
            exit()
        else:
            X = X - a[i]
            if X < 0:
                print("No")
                exit()

if __name__ == '__main__':
    main()