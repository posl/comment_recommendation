def main():
    N, Q = map(int, input().split())
    # あるユーザーがフォローしているユーザーを格納する
    follow = {}
    # あるユーザーをフォローしているユーザーを格納する
    followed_by = {}
    for i in range(1, N+1):
        follow[i] = set()
        followed_by[i] = set()
    for i in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            follow[A].add(B)
            followed_by[B].add(A)
        elif T == 2:
            if A in follow[B]:
                follow[B].remove(A)
            if B in followed_by[A]:
                followed_by[A].remove(B)
        else:
            # A が B をフォローしているかどうか
            if B in follow[A]:
                print("Yes")
            # A が B をフォローしていない場合、A が B をフォローしているユーザーを調べる
            else:
                # A が B をフォローしているユーザーを格納する
                follow_A_B = set()
                for user in follow[A]:
                    follow_A_B.add(user)
                    for user_2 in follow[user]:
                        follow_A_B.add(user_2)
                if B in follow_A_B:
                    print("Yes")
                else:
                    print("No")

if __name__ == '__main__':
    main()