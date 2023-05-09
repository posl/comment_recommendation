def main():
    from collections import defaultdict
    from sys import stdin
    input = stdin.readline
    from bisect import bisect_left,bisect_right
    n=int(input())
    q=[]
    for i in range(n):
        q.append(list(map(int,input().split())))
    s=defaultdict(int)
    max_=0
    min_=10**9
    for i in range(n):
        if q[i][0]==1:
            s[q[i][1]]+=1
            max_=max(max_,q[i][1])
            min_=min(min_,q[i][1])
        elif q[i][0]==2:
            cnt=0
            for key in sorted(s.keys()):
                if cnt>=q[i][2]:
                    break
                if key==q[i][1]:
                    if s[key]>=q[i][2]-cnt:
                        s[key]-=q[i][2]-cnt
                        cnt=q[i][2]
                    else:
                        cnt+=s[key]
                        s[key]=0
                elif key>q[i][1]:
                    break
                else:
                    cnt+=s[key]
                    s[key]=0
            max_=max(s.keys())
            min_=min(s.keys())
        elif q[i][0]==3:
            print(max_-min_)

if __name__ == '__main__':
    main()