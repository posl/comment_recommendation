def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(2**N):
        x = []
        for j in range(N):
            x.append(i>>j&1)
        y = x[0]
        for j in range(1,N):
            if S[j-1]=="AND":
                y = y and x[j]
            else:
                y = y or x[j]
        if y:
            print(i)
            break

if __name__ == '__main__':
    main()