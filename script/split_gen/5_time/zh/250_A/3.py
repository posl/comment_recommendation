def main():
    #input
    H,W=map(int,input().split())
    R,C=map(int,input().split())
    #init
    ans=0
    #calc
    if R==1 or R==H:
        ans+=1
    if C==1 or C==W:
        ans+=1
    #output
    print(ans)
