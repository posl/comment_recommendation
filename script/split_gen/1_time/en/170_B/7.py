def main():
    #input
    X, Y = map(int, input().split())
    #output
    if Y % 2 == 0:
        if X*2 <= Y <= X*4:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
