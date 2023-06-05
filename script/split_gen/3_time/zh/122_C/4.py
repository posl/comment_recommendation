def main():
    N, Q = map(int, input().split())
    S = input()
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    for i in range(Q):
        print(S[query[i][0]-1:query[i][1]].count('AC'))
