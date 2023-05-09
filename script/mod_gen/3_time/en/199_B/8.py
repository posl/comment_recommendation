def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxA = max(A)
    minB = min(B)
    if maxA <= minB:
        print(minB - maxA + 1)
    else:
        print(0)

if __name__ == '__main__':
    main()