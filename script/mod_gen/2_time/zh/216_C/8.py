def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input())
    for i in range(n):
        for j in range(i + 1, n):
            if name_list[i] == name_list[j]:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()