def main():
    #input
    A,B,C,X = map(int,input().split())
    #compute
    if X<A:
        ans = 0
    elif A<=X and X<=B:
        ans = (C/(B-A))
    else:
        ans = 1
    #output
    print(ans)
