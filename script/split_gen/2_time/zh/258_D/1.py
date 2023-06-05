def main():
    n,q = map(int,input().split())
    s = input()
    queries = []
    for _ in range(q):
        queries.append(input().split())
    #print(n,q,s,queries)
    #print(s[int(queries[0][1])-1])
    for i in range(q):
        if int(queries[i][0]) == 1:
            s = s[-1] + s[:-1]
        else:
            print(s[int(queries[i][1])-1])
