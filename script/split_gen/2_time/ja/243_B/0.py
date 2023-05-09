def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_dict = {A[i]: i for i in range(N)}
    B_dict = {B[i]: i for i in range(N)}
    count1 = 0
    count2 = 0
    for i in range(N):
        if A[i] in B_dict and A_dict[A[i]] == B_dict[A[i]]:
            count1 += 1
        if A[i] in B_dict and A_dict[A[i]] != B_dict[A[i]]:
            count2 += 1
    print(count1)
    print(count2)
