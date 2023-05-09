def main():
    T = int(input())
    for i in range(T):
        a,s = map(int, input().split())
        if s < a:
            print("No")
        else:
            if (s - a) % 2 == 0:
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()