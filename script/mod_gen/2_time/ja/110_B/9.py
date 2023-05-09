def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    z = X+1
    while z<=Y:
        if z not in x and z not in y:
            print("No War")
            return
        z += 1
    print("War")
    return

if __name__ == '__main__':
    main()