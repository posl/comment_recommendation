def main():
    N, M = input().split()
    N = int(N)
    M = int(M)
    P = []
    Y = []
    for i in range(M):
        p, y = input().split()
        P.append(int(p))
        Y.append(int(y))
    P = np.array(P)
    Y = np.array(Y)
    P = P - 1
    Y = Y - 1
    Y = Y.astype(str)
    Y = Y.tolist()
    Y = [i.zfill(6) for i in Y]
    P = P.astype(str)
    P = P.tolist()
    P = [i.zfill(6) for i in P]
    P = np.array(P)
    Y = np.array(Y)
    P = P.reshape(M,1)
    Y = Y.reshape(M,1)
    data = np.hstack((P,Y))
    data = data.astype(str)
    data = data.tolist()
    data = ["".join(i) for i in data]
    data = np.array(data)
    data = data.reshape(M,1)
    data = np.sort(data)
    data = data.reshape(M,)
    data = data.tolist()
    data = [i.zfill(12) for i in data]
    for i in range(M):
        print(data[i])

if __name__ == '__main__':
    main()