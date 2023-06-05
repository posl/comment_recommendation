def main():
    line = input()
    a = line.split(" ")
    sum = 0
    for i in range(3):
        sum += int(a[i])
    if sum >= 22:
        print("bust")
    else:
        print("win")

if __name__ == '__main__':
    main()