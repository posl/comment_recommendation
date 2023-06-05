def main():
    a,b,q = map(int,input().split())
    s = [int(input()) for _ in range(a)]
    t = [int(input()) for _ in range(b)]
    x = [int(input()) for _ in range(q)]
    # 二分探索
    def binary_search(array, value):
        left = 0
        right = len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] == value:
                return True
            elif array[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        return False
    # 神社と寺の位置を統合
    st = sorted(s + t)
    # クエリに答える
    for i in range(q):
        ans = float("inf")
        # 神社と寺の位置を二分探索
        idx = binary_search(st, x[i])
        # 神社と寺の位置の間の距離を計算
        if not idx:
            idx = st.index(x[i])
            if idx == 0:
                ans = min(ans, abs(st[idx] - x[i]))
            elif idx == len(st):
                ans = min(ans, abs(st[idx - 1] - x[i]))
            else:
                ans = min(ans, abs(st[idx] - x[i]), abs(st[idx - 1] - x[i]))
        # 神社と寺の位置の間の距離を計算
        else:
            ans = 0
        # 神社と寺の位置の間の距離が最小となるものを出力
        print(ans)
