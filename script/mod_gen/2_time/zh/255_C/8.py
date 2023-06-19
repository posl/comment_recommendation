def main():
    X, A, D, N = map(int, input().split())
    #print(X, A, D, N)
    if D == 0:
        if X != A:
            print("NO")
            return
        else:
            print("YES")
            return
    if N == 1:
        if X == A:
            print("YES")
            return
        else:
            print("NO")
            return
    if (X - A) % D != 0:
        print("NO")
        return
    else:
        if (X - A) // D + 1 <= N:
            print("YES")
            return
        else:
            print("NO")
            return

if __name__ == '__main__':
    main()