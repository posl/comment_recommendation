def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(input())
    for i in range(1,N):
        if W[i-1][-1] != W[i][0] or W[i] in W[:i]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()