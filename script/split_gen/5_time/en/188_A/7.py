def main():
    X,Y = map(int,input().split())
    print('Yes' if X < Y and X+3 > Y else 'No')
