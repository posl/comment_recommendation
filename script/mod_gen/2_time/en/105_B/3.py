def main():
    N = int(input())
    for i in range(N//4+1):
        for j in range(N//7+1):
            if i*4 + j*7 == N:
                print("Yes")
                return
    print("No")
    return

if __name__ == '__main__':
    main()