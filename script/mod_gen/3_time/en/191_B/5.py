def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for a in A:
        if a != X:
            print(a, end=" ")
    print()

if __name__ == '__main__':
    main()