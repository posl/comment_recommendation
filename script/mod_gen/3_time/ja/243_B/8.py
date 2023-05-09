def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    A_dict = {A[i]: i for i in range(N)}
    B_dict = {B[i]: i for i in range(N)}
    A_B_dict = {A[i]: B[i] for i in range(N)}
    A_B_dict2 = {B[i]: A[i] for i in range(N)}
    #print(A_dict)
    #print(B_dict)
    #print(A_B_dict)
    #print(A_B_dict2)
    count1 = 0
    count2 = 0
    for i in range(N):
        if A[i] == B[i]:
            count1 += 1
        elif A_B_dict[A[i]] == B[i]:
            count2 += 1
        elif A_B_dict2[B[i]] == A[i]:
            count2 += 1
    print(count1)
    print(count2)

if __name__ == '__main__':
    main()