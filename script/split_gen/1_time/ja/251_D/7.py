def main():
    W = int(input())
    if W % 2 == 1:
        print(W+1)
        for i in range(W):
            print(1, end=' ')
        print()
    else:
        print(W)
        for i in range(W):
            print(1, end=' ')
        print()
