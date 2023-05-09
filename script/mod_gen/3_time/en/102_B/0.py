def main():
    N = int(input())
    A = list(map(int, input().split()))
    maxA = max(A)
    minA = min(A)
    print(maxA - minA)
main()

if __name__ == '__main__':
    main()