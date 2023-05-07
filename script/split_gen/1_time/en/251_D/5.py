def main():
    W = int(input())
    N = W // 2
    if W % 2 == 0:
        print(N)
        for i in range(N):
            print(2)
    else:
        print(N + 1)
        for i in range(N):
            print(2)
        print(1)
