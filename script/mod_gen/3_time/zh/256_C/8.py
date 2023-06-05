def main():
    h1,h2,h3,w1,w2,w3=map(int,input().split())
    res=0
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                if i+j+k==h1 and i+j+k==h2 and i+j+k==h3 and i+j+k==w1 and i+j+k==w2 and i+j+k==w3:
                    res+=1
    print(res)

if __name__ == '__main__':
    main()