def main():
    N,K = map(int,input().split())
    A = []
    for i in range(N):
        A.append(list(map(int,input().split())))
    A.sort()
    A = list(zip(*A))
    A.sort()
    A = list(zip(*A))
    A = list(zip(*A))
    A.sort()
    A = list(z

if __name__ == '__main__':
    main()