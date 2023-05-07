def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # print(N)
    # print(A)
    # print(B)
    # A = [1,3,5]
    # B = [3,-6,3]
    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    if sum == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()