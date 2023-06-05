def main():
    N = int(input())
    for i in range(0, N):
        for j in range(0, N):
            if (4*i+7*j) == N:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()