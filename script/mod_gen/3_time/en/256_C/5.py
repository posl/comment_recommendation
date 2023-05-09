def main():
    h1,h2,h3,w1,w2,w3=map(int,input().split())
    ans=0
    for i in range(1,h1+1):
        for j in range(1,w1+1):
            if i+j==h1 and i*j==w1:
                for k in range(1,h2+1):
                    for l in range(1,w2+1):
                        if k+l==h2 and k*l==w2:
                            for m in range(1,h3+1):
                                for n in range(1,w3+1):
                                    if m+n==h3 and m*n==w3:
                                        if i+k+m==j+l+n:
                                            ans+=1
    print(ans)
main()
The author's solution

if __name__ == '__main__':
    main()