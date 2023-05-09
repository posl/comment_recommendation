def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #Aの各要素の出現回数を数える
    A_count = [0] * (N + 1)
    for i in range(N):
        A_count[A[i]] += 1
    #Bの各要素の出現回数を数える
    B_count = [0] * (N + 1)
    for i in range(N):
        B_count[B[i]] += 1
    #Cの各要素の出現回数を数える
    C_count = [0] * (N + 1)
    for i in range(N):
        C_count[C[i]] += 1
    #Bの各要素の出現回数を数える
    B_count = [0] * (N + 1)
    for i in range(N):
        B_count[B[i]] += 1
    ans = 0
    for i in range(1, N + 1):
        ans += A_count[i] * C_count[i] * B_count[i]
    print(ans)

if __name__ == '__main__':
    main()