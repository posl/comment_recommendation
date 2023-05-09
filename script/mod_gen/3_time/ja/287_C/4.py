def main():
    N, M = map(int, input().split())
    if M != N-1:
        print("No")
        return
    for i in range(M):
        u, v = map(int, input().split())
        if u > N or v > N:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()