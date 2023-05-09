def main():
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    for b in B:
        if b not in A:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()