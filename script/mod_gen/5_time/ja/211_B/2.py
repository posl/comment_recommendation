def main():
    list = []
    for i in range(4):
        list.append(input())
    if "H" in list and "2B" in list and "3B" in list and "HR" in list:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()