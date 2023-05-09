def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(input())
    if len(set(W)) != N:
        print("No")
        return
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()