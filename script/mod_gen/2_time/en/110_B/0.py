def main():
    N, M, X, Y = [int(x) for x in input().split()]
    x = [int(x) for x in input().split()]
    y = [int(x) for x in input().split()]
    x.append(X)
    y.append(Y)
    x.sort()
    y.sort()
    if x[-1] < y[0]:
        print("No War")
    else:
        print("War")

if __name__ == '__main__':
    main()