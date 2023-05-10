def main():
    N, Q = map(int, input().split())
    S = input()
    query = [list(map(str, input().split())) for i in range(Q)]
    for i in range(Q):
        if query[i][0] == "1":
            S = S[-int(query[i][1]):] + S[:-int(query[i][1])]
        else:
            print(S[int(query[i][1])-1])
