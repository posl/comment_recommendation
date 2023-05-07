def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for a in A:
        if a < P:
            count += 1
    print(count)

if __name__ == '__main__':
    main()