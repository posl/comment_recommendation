def main():
    N,M = map(int,input().split())
    for i in range(M):
        k,*x = map(int,input().split())
        for j in range(k):
            for l in range(j+1,k):
                if x[j] == x[l]:
                    print("No")
                    exit()
    print("Yes")

if __name__ == '__main__':
    main()