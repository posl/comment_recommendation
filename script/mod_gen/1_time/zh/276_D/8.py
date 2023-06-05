def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        if all(a % 2 == 0 for a in A):
            A = [a / 2 for a in A]
            count += 1
        else:
            break
    print(count)

if __name__ == '__main__':
    main()