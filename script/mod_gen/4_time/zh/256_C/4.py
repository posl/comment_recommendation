def main():
    h1,h2,h3,w1,w2,w3 = map(int,input().split())
    #print(h1,h2,h3,w1,w2,w3)
    #print(h1+h2+h3,w1+w2+w3)
    #print(h1+h2+h3-w1-w2-w3)
    if h1+h2+h3==w1+w2+w3:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()