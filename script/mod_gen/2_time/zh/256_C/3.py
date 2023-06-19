def main():
    h1,h2,h3,w1,w2,w3 = map(int,input().split())
    print(h1,h2,h3,w1,w2,w3)
    #print(h1+h2+h3,w1+w2+w3)
    if h1+h2+h3 != w1+w2+w3:
        print(0)
        return
    #print('h1+h2+h3 == w1+w2+w3')
    #print(h1,h2,h3,w1,w2,w3)
    if h1+w1 != h2+w2:
        print(0)
        return
    if h1+w1 != h3+w3:
        print(0)
        return
    #print('h1+w1 == h2+w2 == h3+w3')
    #print(h1,h2,h3,w1,w2,w3)
    if h1 == w1:
        print(1)
        return
    if h1 == w2:
        print(1)
        return
    if h1 == w3:
        print(1)
        return
    if h2 == w1:
        print(1)
        return
    if h2 == w2:
        print(1)
        return
    if h2 == w3:
        print(1)
        return
    if h3 == w1:
        print(1)
        return
    if h3 == w2:
        print(1)
        return
    if h3 == w3:
        print(1)
        return
    print(0)
    return

if __name__ == '__main__':
    main()