def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_max = max(A)
    B_min = min(B)
    if B_min < A_max:
        print(0)
    else:
        print(B_min - A_max + 1)

if __name__ == '__main__':
    main()