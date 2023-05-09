def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    # 0 は L に置き換える
    # N は R に置き換える
    # 0 と N 以外は L と R のどちらか小さい方に置き換える
    # 0 と N 以外をすべて L に置き換える
    # 0 と N 以外をすべて R に置き換える
    # 0 と N 以外をすべて L に置き換える
    ans1 = 0
    for i in range(N):
        ans1 += min(A[i], L)
    # 0 と N 以外をすべて R に置き換える
    ans2 = 0
    for i in range(N):
        ans2 += min(A[i], R)
    # 0 は L に置き換える
    # N は R に置き換える
    # 0 と N 以外は L と R のどちらか小さい方に置き換える
    ans3 = 0
    for i in range(N):
        if i < N // 2:
            ans3 += min(A[i], L)
        else:
            ans3 += min(A[i], R)
    print(min(ans1, ans2, ans3))
