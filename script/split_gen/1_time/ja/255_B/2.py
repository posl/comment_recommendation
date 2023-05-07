def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    
    # 人 i が人 j を照らす時の明かりの強さ
    R = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            R[i][j] = ((X[i] - X[j])**2 + (Y[i] - Y[j])**2)**0.5
    
    # 人 i が人 j を照らす時の明かりの強さの最小値
    R_min = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                R_min[i][j] = 0
            else:
                R_min[i][j] = min(R[i][j], R_min[j][i])
    
    # 人 i を照らす明かりの強さの最大値
    R_max = [0 for _ in range(N)]
    for i in range(N):
        R_max[i] = max([R_min[i][j] for j in range(N)])
    
    # 人 i が人 j を照らす時の明かりの強さの最小値の最大値
    R_max_max = 0
    for i in range(N):
        R_max_max = max(R_max_max, min([R_min[i][j] for j in range(N)]))
    
    # 人 i が人 j を照らす時の明かりの強さの最小値の最大値の最小値
    R_max_max_min = 10**10
    for i in range(N):
        R_max_max_min = min(R_max_max_min, min([R_min[i][j] for j in range(N)]))
    
    # 人 i が人 j を照らす時の明かりの強さの最小
