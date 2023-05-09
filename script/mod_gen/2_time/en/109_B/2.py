def main():
    N = int(input())
    W = [input() for i in range(N)]
    if len(set(W)) == N:
        for i in range(N-1):
            if W[i][-1] != W[i+1][0]:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()