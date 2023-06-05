def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            print(0)
            return
        else:
            print(1)
            return
    if (X - A) % D != 0:
        print(-1)
        return
    else:
        if (X - A) // D < 0:
            print(-1)
            return
        else:
            if (X - A) // D + 1 > N:
                print(-1)
                return
            else:
                print(N - ((X - A) // D + 1))
                return

if __name__ == '__main__':
    main()