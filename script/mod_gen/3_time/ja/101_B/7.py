def main():
    N = input()
    s = sum([int(i) for i in N])
    if int(N)%s == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()