def main():
    # read input
    N = int(input())
    L = []
    for _ in range(N):
        l = list(map(int,input().split()))
        L.append(l[1:])
    
    # count
    count = 0
    for i in range(N):
        if L[i] != []:
            count += 1
            for j in range(i+1,N):
                if L[i] == L[j]:
                    L[j] = []
    
    # print result
    print(count)
main()

if __name__ == '__main__':
    main()