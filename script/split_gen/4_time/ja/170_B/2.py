def main():
    X, Y = map(int, input().split())
    for i in range(X+1):
        if i*4 + (X-i)*2 == Y:
            print('Yes')
            return
    print('No')
