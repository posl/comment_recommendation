def main():
    n = int(input())
    list1 = []
    for i in range(n):
        list1.append(input())
    if len(list1) == len(set(list1)):
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()