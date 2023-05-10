def main():
    h1,h2,h3,w1,w2,w3 = map(int,input().split())
    if h1+w2==h2+w1 and h2+w3==h3+w2 and h1+w3==h3+w1:
        print('1')
    else:
        print('0')
