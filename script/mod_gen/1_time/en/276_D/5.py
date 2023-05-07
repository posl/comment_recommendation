def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        if all([a % 2 == 0 for a in A]):
            A = [a // 2 for a in A]
            count += 1
        elif all([a % 3 == 0 for a in A]):
            A = [a // 3 for a in A]
            count += 1
        else:
            break
    if all([a == A[0] for a in A]):
        print(count)
    else:
        print(-1)

if __name__ == '__main__':
    main()