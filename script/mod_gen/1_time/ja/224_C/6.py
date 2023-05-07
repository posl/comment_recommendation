def main():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i],Y[i] = map(int, input().split())
    cnt = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if ((X[j]-X[i])*(Y[k]-Y[i])-(X[k]-X[i])*(Y[j]-Y[i])) != 0:
                    cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()