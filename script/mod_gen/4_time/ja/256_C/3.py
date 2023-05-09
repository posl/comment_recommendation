def main():
    h1,h2,h3,w1,w2,w3 = map(int,input().split())
    if h1+h2+h3 == w1+w2+w3:
        print(1)
    else:
        print(0)
main()

if __name__ == '__main__':
    main()