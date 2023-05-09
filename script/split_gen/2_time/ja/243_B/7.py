def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #Aの要素をkey、インデックスをvalueにした辞書
    A_dic = {A[i]: i for i in range(N)}
    #Bの要素をkey、インデックスをvalueにした辞書
    B_dic = {B[i]: i for i in range(N)}
    #AにもBにも含まれ、その位置も一致している整数の個数
    count_match = 0
    #AにもBにも含まれるが、その位置は異なる整数の個数
    count_diff = 0
    #AにもBにも含まれるが、その位置は異なる整数の組のリスト
    diff_list = []
    #AにもBにも含まれるが、その位置は異なる整数の組のリストを作成
    for i in range(N):
        if A[i] in B:
            if A_dic[A[i]] == B_dic[A[i]]:
                count_match += 1
            else:
                diff_list.append((A[i], B[B_dic[A[i]]]))
    #diff_listから重複を除く
    diff_list = list(set(diff_list))
    #AにもBにも含まれるが、その位置は異なる整数の個数
    count_diff = len(diff_list)
    #出力
    print(count_match)
    print(count_diff)
