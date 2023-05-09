def main():
    N,A,B = map(int,input().split())
    for i in range(N*A):
        if i%N < N//2:
            print("."*(N*B))
        else:
            print("#"*(N*B))

if __name__ == '__main__':
    main()