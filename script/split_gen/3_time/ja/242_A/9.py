def main():
    A,B,C,X = map(int,input().split())
    print((C/B)*((B-C)/(B-A))**(X-A-1))
