def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # print(A)
    # print(B)
    # print(N)
    # print(M)
    # 1からNまでの値を持つリストを作る
    # 1からNまでの値を持つリストのうち、1とNを除いたものを作る
    # 1からNまでの値を持つリストのうち、1とNを除いたものの中から、Aの値を持たないものを作る
    # 1からNまでの値を持つリストのうち、1とNを除いたものの中から、Bの値を持たないものを作る
    # 1からNまでの値を持つリストのうち、1とNを除いたものの中から、AとBの値を持たないものを作る
    # 1からNまでの値を持つリストのうち、1とNを除いたものの中から、AとBの値を持たないものの中で、最大の値を持つものを選ぶ
    # 1からNまでの値を持つリストを作る
    all_list = []
    for i in range(1, N+1):
        all_list.append(i)
    # print(all_list)
    # 1からNまでの値を持つリストのうち、1とNを除いたものを作る
    all_list2 = []
    for i in all_list:
        if i != 1 and i != N:
            all_list2.append(i)
    # print(all_list2)
    # 1からNまでの値を持つリストのうち、1とNを除いたものの中から、Aの値を持たないもの
