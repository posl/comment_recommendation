def main():
    N = input()
    s = 0
    for i in N:
        s += int(i)
    if s % 9 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()