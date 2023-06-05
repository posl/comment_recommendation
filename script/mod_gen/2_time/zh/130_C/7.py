def problem130_b():
    N,X = map(int,input().split())
    L = list(map(int,input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i]+L[i])
    print(len([i for i in D if i<=X]))

if __name__ == '__main__':
    problem130_b()