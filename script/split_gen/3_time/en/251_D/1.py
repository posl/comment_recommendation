def main():
    W = int(input())
    if W%2 == 0:
        print(W//2)
        print(' '.join([str(x) for x in range(1,W//2+1)]))
    else:
        print(W//2+1)
        print(' '.join([str(x) for x in range(1,W//2+2)]))
