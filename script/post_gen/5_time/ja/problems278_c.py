Synthesizing 10/10 solutions

=======
Suggestion 1

def check_follow(user, follow):
    if user in follow:
        return True
    else:
        return False

=======
Suggestion 2

def check_follow(a, b, follows):
    if a in follows[b] and b in follows[a]:
        return True
    else:
        return False

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    follow = {}
    for i in range(1, N+1):
        follow[i] = set()
    for _ in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a].add(b)
        elif t == 2:
            follow[a].discard(b)
        else:
            if b in follow[a]:
                print('Yes')
            else:
                print('No')

=======
Suggestion 4

def check_follow(user1, user2, follow_list):
    if user1 in follow_list[user2]:
        return True
    else:
        return False

=======
Suggestion 5

def check_follow(user1, user2, follow_list):
    if user1 in follow_list[user2] and user2 in follow_list[user1]:
        return True
    else:
        return False

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    a = []
    for i in range(q):
        a.append(list(map(int, input().split())))
    #print(a)
    #print(n)
    #print(q)

    # ユーザーがフォローしているユーザーの辞書
    # ユーザーの番号をキーとする
    # ユーザー番号のリストを値とする
    user = {}
    for i in range(1, n+1):
        user[i] = []
    #print(user)

    # ユーザーのフォローを判定する
    # ユーザーがフォローしているユーザーのリストを見て、
    # 指定されたユーザーが含まれているかを判定する
    def follow(a, b):
        #print(a, b)
        if b in user[a]:
            return True
        else:
            return False

    # ユーザーのフォローを判定する
    # ユーザーがフォローしているユーザーのリストを見て、
    # 指定されたユーザーが含まれているかを判定する
    def follow2(a, b):
        #print(a, b)
        if a in user[b]:
            return True
        else:
            return False

    # ユーザーがフォローしているユーザーのリストに
    # 指定されたユーザーを追加する
    def add(a, b):
        #print(a, b)
        user[a].append(b)

    # ユーザーがフォローしているユーザーのリストから
    # 指定されたユーザーを削除する
    def remove(a, b):
        #print(a, b)
        user[a].remove(b)

    # ユーザーのフォローを判定する
    #

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    follow = [set() for i in range(N)]
    for i in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a-1].add(b-1)
        elif t == 2:
            follow[a-1].discard(b-1)
        else:
            if b-1 in follow[a-1] and a-1 in follow[b-1]:
                print("Yes")
            else:
                print("No")
    return

=======
Suggestion 8

def main():
    n, q = map(int, input().split())
    follow = [[False for i in range(n)] for j in range(n)]
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a-1][b-1] = True
        elif t == 2:
            follow[a-1][b-1] = False
        else:
            if follow[a-1][b-1]:
                print("Yes")
            else:
                print("No")

=======
Suggestion 9

def main():
    n, q = map(int, input().split())
    follow = {}
    for i in range(1, n+1):
        follow[i] = set()

    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a].add(b)
        elif t == 2:
            follow[a].discard(b)
        else:
            if b in follow[a]:
                print('Yes')
            else:
                print('No')

=======
Suggestion 10

def main():
    pass
