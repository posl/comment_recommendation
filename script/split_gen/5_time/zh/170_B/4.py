def main():
    X,Y = map(int,input().split())
    if Y%2 == 0:
        if Y/2 <= X <= Y/4:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
