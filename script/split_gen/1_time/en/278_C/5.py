def main():
    N, Q = map(int, input().split())
    # フォロー関係を管理するリスト
    follow = [set() for _ in range(N)]
    # フォローの逆関係を管理するリスト
    follower = [set() for _ in range(N)]
    for _ in range(Q):
        T, A, B = map(int, input().split())
        A -= 1
        B -= 1
        # フォロー関係の登録
        if T == 1:
            follow[A].add(B)
            follower[B].add(A)
        # フォロー関係の解除
        elif T == 2:
            follow[A].discard(B)
            follower[B].discard(A)
        # フォロー関係の判定
        else:
            if B in follow[A] and A in follow[B]:
                print("Yes")
            else:
                print("No")
