def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0:
        print("Yes")
    else:
        for i in range(N//4):
            for j in range(N//7):
                if i*4 + j*7 == N:
                    print("Yes")
                    return
        print("No")
        return

if __name__ == '__main__':
    main()