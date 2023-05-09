def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    print((h1*h2*h3*w1*w2*w3)//(h1*h2*w3+h2*h3*w1+h3*h1*w2))

if __name__ == '__main__':
    main()