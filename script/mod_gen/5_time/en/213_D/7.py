def main():
    N = int(input())
    AB = []
    for i in range(N-1):
        AB.append(list(map(int, input().split())))
    print(AB)
    return

if __name__ == '__main__':
    main()