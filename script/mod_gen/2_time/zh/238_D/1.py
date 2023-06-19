def main():
    n = int(input())
    for i in range(n):
        a, s = map(int, input().split())
        if (a ^ s) & (a & s) == 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()