def main():
    N = int(input())
    W = [input() for _ in range(N)]
    if len(set(W)) != N:
        print("No")
        return
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print("No")
            return
    print("Yes")
    return
main()

if __name__ == '__main__':
    main()