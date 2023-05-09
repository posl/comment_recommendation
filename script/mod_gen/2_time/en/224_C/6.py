def get_input():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    return N,X,Y

if __name__ == '__main__':
    get_input()