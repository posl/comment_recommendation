def isMatch(S, T):
    # 逆时针旋转90度，顺时针旋转270度
    def rotate(S):
        return list(zip(*S[::-1]))
    # 水平翻转
    def reflect(S):
        return [row[::-1] for row in S]
    # 判断S和T是否完全匹配
    def equal(S, T):
        for i in range(N):
            for j in range(N):
                if S[i][j] != T[i][j]:
                    return False
        return True
    N = len(S)
    for _ in range(4):
        if equal(S, T):
            return True
        S = rotate(S)
    S = reflect(S)
    if equal(S, T):
        return True
    for _ in range(3):
        if equal(S, T):
            return True
        S = rotate(S)
    return False
N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]

if __name__ == '__main__':
    isMatch()