def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    # 10^100 copies of A
    B = []
    for i in range(100):
        B += A
    # sum up from left to right
    # when does the sum exceed X for the first time?
    sum = 0
    for i in range(len(B)):
        sum += B[i]
        if sum > X:
            print(i + 1)
            break

if __name__ == '__main__':
    main()