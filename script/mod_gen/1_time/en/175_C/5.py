def main():
    X, K, D = map(int, input().split())
    if X >= 0:
        if K <= X // D:
            print(X - K * D)
        else:
            if (K - X // D) % 2 == 0:
                print(X % D)
            else:
                print(abs(X % D - D))
    else:
        if K <= abs(X) // D:
            print(abs(X) - K * D)
        else:
            if (K - abs(X) // D) % 2 == 0:
                print(abs(X) % D)
            else:
                print(abs(abs(X) % D - D))

if __name__ == '__main__':
    main()