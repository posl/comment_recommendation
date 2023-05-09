def main():
    N = int(input())
    for i in range(0, N+1, 4):
        if (N-i)%7 == 0:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()