def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 90度の判定
    def judge90(x1, y1, x2, y2):
        if x1 * x2 + y1 * y2 == 0:
            return True
        else:
            return False
    
    # 2点間の距離の判定
    def judgeDist(x1, y1, x2, y2, dist):
        if (x1 - x2)**2 + (y1 - y2)**2 == dist**2:
            return True
        else:
            return False
    
    # 答え
    ans = "Yes"
    
    # 初期値
    x1, y1 = 0, 0
    x2, y2 = A[0], 0
    # 2点間の距離の判定
    if not judgeDist(x1, y1, x2, y2, A[0]):
        ans = "No"
    # 90度の判定
    if not judge90(x2, y2, x, y):
        ans = "No"
    
    for i in range(1, N):
        # 2点間の距離の判定
        if not judgeDist(x2, y2, x, y, A[i]):
            ans = "No"
        # 90度の判定
        if not judge90(x1, y1, x2, y2):
            ans = "No"
        
        x1, y1 = x2, y2
        x2, y2 = x, y
    
    # 2点間の距離の判定
    if not judgeDist(x2, y2, x, y, A[N-1]):
        ans = "No"
    
    print(ans)
