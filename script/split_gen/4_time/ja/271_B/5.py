def main():
    N, Q = map(int, input().split())
    #数列を格納する配列
    a_list = []
    for i in range(N):
        a_list.append(list(map(int, input().split())))
    #クエリを格納する配列
    query_list = []
    for i in range(Q):
        query_list.append(list(map(int, input().split())))
    for i in range(Q):
        print(a_list[query_list[i][0]-1][query_list[i][1]-1])
