def problems273_b():
    X,K = input().split()
    K = int(K)
    num = int(X)
    for i in range(K):
        num = round(num, -i-1)
    print(num)

if __name__ == '__main__':
    problems273_b()