def main():
    n, q = map(int, input().split())
    # 各ユーザーのフォローしているユーザーのリスト
    followed_by = [[] for _ in range(n)]
    # 各ユーザーのフォローされているユーザーのリスト
    following = [[] for _ in range(n)]
    for _ in range(q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            followed_by[a].append(b)
            following[b].append(a)
        elif t == 2:
            if b in followed_by[a]:
                followed_by[a].remove(b)
                following[b].remove(a)
        else:
            if any(f in followed_by[a] for f in following[b]):
                print("Yes")
            else:
                print("No")
