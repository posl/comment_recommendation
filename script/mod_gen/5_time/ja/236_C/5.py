def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    S_index = 0
    T_index = 0
    for i in range(N):
        if S[S_index] == T[T_index]:
            T_index += 1
            if T_index == M:
                print("Yes")
                return
        S_index += 1
    print("No")
main()

if __name__ == '__main__':
    main()