def main():
    N = int(input())
    if (N == 1):
        print(1)
        return
    if (N == 2):
        print(2)
        return
    i = 1
    while (i * (i + 1) // 2 < N):
        i += 1
    print(i)
    return

if __name__ == '__main__':
    main()