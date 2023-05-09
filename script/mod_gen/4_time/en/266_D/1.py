def main():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    #print(N)
    #print(T)
    #print(X)
    #print(A)
    # 1. T_1 < T_2 < ... < T_N
    # 2. 0 < T_1
    # 3. T_N <= 10^5
    # 4. 0 <= X_i <= 4
    # 5. 1 <= A_i <= 10^9
    # 6. 1 <= N <= 10^5
    # 7. Takahashi is at coordinate 0 at time 0
    # 8. Takahashi can move on the line at a speed of at most 1.
    # 9. He can catch a Snuke appearing from a pit if and only if he is at the coordinate of that pit exactly when it appears.
    # 10. The time it takes to catch a Snuke is negligible.
    # 1. Takahashi is at coordinate 0 at time 0
    # 2. Takahashi can move on the line at a speed of at most 1.
    # 3. He can catch a Snuke appearing from a pit if and only if he is at the coordinate of that pit exactly when it appears.
    # 4. The time it takes to catch a Snuke is negligible.
    # 1. Takahashi is at coordinate 0 at time 0
    # 2. He can catch a Snuke appearing from a pit if and only if he is at the coordinate of that pit exactly when it appears.
    # 3. The time it takes to catch a Snuke is negligible.
    # 1. Takahashi is at coordinate 0 at time 0
    # 2. He can catch a Snuke appearing from a pit if and only if he is at the coordinate of that pit exactly when it appears.
    # Takahashi can catch a Snuke appearing from a pit if and only if he is at the coordinate of that pit exactly when it

if __name__ == '__main__':
    main()