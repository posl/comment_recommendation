def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return
    else:
        for i in range(M):
            u, v = map(int, input().split())
            if u == 1 or v == 1:
                pass
            else:
                print("No")
                return
        print("Yes")
        return

if __name__ == '__main__':
    main()