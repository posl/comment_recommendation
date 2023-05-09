def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxA = max(A)
    minB = min(B)
    if maxA > minB:
        print(0)
    else:
        print(minB - maxA + 1)

if __name__ == '__main__':
    main()