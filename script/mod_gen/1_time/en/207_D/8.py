def main():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    T = [list(map(int, input().split())) for _ in range(N)]
    def same(S, T):
        for i in range(N):
            for j in range(N):
                if S[i][0] == T[j][0] and S[i][1] == T[j][1]:
                    break
            else:
                return False
        return True
    def rotate(S, theta):
        return [[S[i][0] * cos(theta) - S[i][1] * sin(theta), S[i][0] * sin(theta) + S[i][1] * cos(theta)] for i in range(N)]
    def translate(S, dx, dy):
        return [[S[i][0] + dx, S[i][1] + dy] for i in range(N)]
    if same(S, T):
        print('Yes')
        return
    for i in range(4):
        S = rotate(S, pi / 2)
        if same(S, T):
            print('Yes')
            return
    for dx in range(-100, 101):
        for dy in range(-100, 101):
            S = translate(S, dx, dy)
            if same(S, T):
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()