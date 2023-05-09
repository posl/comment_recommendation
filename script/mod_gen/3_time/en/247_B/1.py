def main():
    N = int(input())
    S = [0] * N
    T = [0] * N
    for i in range(N):
        S[i], T[i] = input().split()
    for i in range(N):
        for j in range(N):
            if i != j:
                if S[i] == S[j] or T[i] == T[j]:
                    print("No")
                    return
    print("Yes")

if __name__ == '__main__':
    main()