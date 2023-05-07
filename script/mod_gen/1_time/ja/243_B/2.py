def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_dict = {A[i]: i for i in range(N)}
    B_dict = {B[i]: i for i in range(N)}
    A_B = [A_dict[i] for i in B if i in A_dict]
    B_A = [B_dict[i] for i in A if i in B_dict]
    print(len(set(A_B)))
    print(len(set(A_B) & set(B_A)))

if __name__ == '__main__':
    main()