def main():
    N = int(input())
    A = list(map(int,input().split(" ")))
    max = 0
    for l in range(1,N+1):
        for r in range(l,N+1):
            for x in range(1,100000):
                if x > max:
                    flag = True
                    for i in range(l-1,r):
                        if x > A[i]:
                            flag = False
                            break
                    if flag:
                        max = x
    print(max)

if __name__ == '__main__':
    main()