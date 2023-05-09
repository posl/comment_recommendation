def main():
    W = int(input())
    if W % 2 == 0:
        print(W//2)
        print(' '.join([str(2)]*(W//2)))
    else:
        print(W//2 + 1)
        print(' '.join([str(2)]*(W//2) + [str(1)]))
