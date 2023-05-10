def solve():
    N = int(input())
    X = []
    Y = []
    P = []
    for _ in range(N):
        x, y, p = map(int, input().split())
        X.append(x)
        Y.append(y)
        P.append(p)
    def can_jump(i, j, S):
        return P[i] * S >= abs(X[i] - X[j]) + abs(Y[i] - Y[j])
    def can_jump_from_start(i, S):
        return can_jump(0, i, S)
    def can_jump_to_goal(i, S):
        return can_jump(i, N - 1, S)
    def can_jump_from_start_to_goal(S):
        for i in range(1, N - 1):
            if not can_jump_from_start(i, S):
                return False
        return True
    def can_jump_to_goal_from_start(S):
        for i in range(1, N - 1):
            if not can_jump_to_goal(i, S):
                return False
        return True
    def can_jump_from_start_to_goal_with_S(S):
        if can_jump_from_start_to_goal(S) or can_jump_to_goal_from_start(S):
            return True
        for i in range(1, N - 1):
            if can_jump_from_start(i, S) and can_jump_to_goal(i, S):
                return True
        return False
    def can_jump_from_start_to_goal_with_S_plus_1(S):
        if can_jump_from_start_to_goal(S + 1) or can_jump_to_goal_from_start(S + 1):
            return True
        for i in range(1, N - 1):
            if can_jump_from_start(i, S + 1) and can_jump_to_goal(i, S + 1):
                return True
        return False
    S = 0
    while not can_jump_from_start_to_goal_with_S(S):
        S += 1
    while can_jump_from_start_to_goal_with_S_plus_1(S):
        S += 1
    print(S)

if __name__ == '__main__':
    solve()