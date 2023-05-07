def main():
    n = int(input())
    for_list = []
    for i in range(n):
        for_list.append(input())
    if for_list.count("For") > n//2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()