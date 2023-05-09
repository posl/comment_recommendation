def main():
    n = input()
    #print(n)
    sum = 0
    for i in n:
        sum += int(i)
    #print(sum)
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()