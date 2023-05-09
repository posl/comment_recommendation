def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input().split())
    name_list.sort()
    for i in range(n-1):
        if name_list[i][0] == name_list[i+1][0] and name_list[i][1] == name_list[i+1][1]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()