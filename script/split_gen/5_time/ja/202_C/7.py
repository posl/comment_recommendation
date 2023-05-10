def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B_dict = {}
    for i in range(len(B)):
        B_dict[B[i]-1] = i
    C_dict = {}
    for i in range(len(C)):
        if C[i]-1 in B_dict:
            if B_dict[C[i]-1] in C_dict:
                C_dict[B_dict[C[i]-1]] += 1
            else:
                C_dict[B_dict[C[i]-1]] = 1
    count = 0
    for i in range(len(A)):
        if A[i]-1 in C_dict:
            count += C_dict[A[i]-1]
    print(count)
