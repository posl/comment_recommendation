def main():
    from sys import stdin
    from collections import Counter
    read=stdin.readline
    N=int(read())
    S=Counter()
    S_max=0
    S_min=10**9
    for i in range(N):
        query=read().split()
        if query[0]=='1':
            S[int(query[1])]+=1
            S_max=max(S_max,int(query[1]))
            S_min=min(S_min,int(query[1]))
        elif query[0]=='2':
            if S[int(query[1])]>0:
                if S[int(query[1])]<int(query[2]):
                    S_min=max(S_min,int(query[1]))
                    S[int(query[1])]-=S[int(query[1])]
                else:
                    S[int(query[1])]-=int(query[2])
        else:
            print(S_max-S_min)
