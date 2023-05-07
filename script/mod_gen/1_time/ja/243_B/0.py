def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_dict = {}
    B_dict = {}
    for i in range(N):
        A_dict[A[i]] = i
        B_dict[B[i]] = i
    count1 = 0
    count2 = 0
    for i in range(N):
        if A_dict[A[i]] == B_dict[A[i]]:
            count1 += 1
        else:
            count2 += 1
    print(count1)
    print(count2)

if __name__ == '__main__':
    main()