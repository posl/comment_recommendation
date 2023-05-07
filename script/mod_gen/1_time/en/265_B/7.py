def main():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    bonus = []
    for i in range(M):
        bonus.append(list(map(int,input().split())))
    t = T
    for i in range(N-1):
        t -= A[i]
        if t <= 0:
            print("No")
            return
        if bonus and bonus[0][0] == i+1:
            t += bonus[0][1]
            bonus.pop(0)
    print("Yes")
    return

if __name__ == '__main__':
    main()