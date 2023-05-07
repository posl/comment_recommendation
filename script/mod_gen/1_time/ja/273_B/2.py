def main():
    X, K = map(int, input().split())
    print(X - X % (10 ** K) + (10 ** K if X % (10 ** K) >= (10 ** K) / 2 else 0))

if __name__ == '__main__':
    main()