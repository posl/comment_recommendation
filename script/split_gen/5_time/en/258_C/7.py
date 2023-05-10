def main():
    N,Q = map(int,input().split())
    S = input()
    query = []
    for _ in range(Q):
        query.append(list(map(str,input().split())))
    for q in query:
        if q[0] == '1':
            S = S[-int(q[1]):] + S[:-int(q[1])]
        else:
            print(S[int(q[1])-1])
