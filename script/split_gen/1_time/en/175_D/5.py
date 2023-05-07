def main():
    N,K=map(int,input().split())
    P=list(map(int,input().split()))
    C=list(map(int,input().split()))
    ans=-float('inf')
    for i in range(N):
        j=i
        score=0
        count=0
        while count<K:
            score+=C[P[j]-1]
            if score>ans:
                ans=score
            j=P[j]-1
            count+=1
            if j==i:
                break
        if count<K:
            loop=K//count
            score*=loop
            if score>ans:
                ans=score
            count+=loop*count
            while count<K:
                score+=C[P[j]-1]
                if score>ans:
                    ans=score
                j=P[j]-1
                count+=1
    print(ans)
