def main():
    N = int(input())
    for i in range(N+1):
        for j in range(N+1):
            if 4*i+7*j == N:
                print("Yes")
                return
    print("No")
    return

if __name__ == '__main__':
    main()