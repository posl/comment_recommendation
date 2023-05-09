def main():
    N = input()
    if N == "0":
        print("Yes")
        return
    sum = 0
    for i in N:
        sum += int(i)
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()