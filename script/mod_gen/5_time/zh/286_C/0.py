def main():
    N, A, B = map(int, input().split())
    S = input()
    A_count = 0
    B_count = 0
    for i in range(N//2):
        if S[i] != S[-i-1]:
            if S[i] == "a":
                A_count += 1
            else:
                B_count += 1
    if A_count == 0 and B_count == 0:
        print(0)
    else:
        print(A_count*A+B_count*B)

if __name__ == '__main__':
    main()