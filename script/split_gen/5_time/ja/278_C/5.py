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
