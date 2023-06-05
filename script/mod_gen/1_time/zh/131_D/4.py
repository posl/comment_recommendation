def main():
    N = int(input())
    AB = [[int(i) for i in input().split()] for j in range(N)]
    AB.sort(key=lambda x: x[1])
    t = 0
    for ab in AB:
        t += ab[0]
        if t > ab[1]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()