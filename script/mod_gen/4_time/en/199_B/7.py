def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    minB = min(B)
    maxA = max(A)
    if maxA > minB:
        print(0)
    else:
        print(minB - maxA + 1)

if __name__ == '__main__':
    main()