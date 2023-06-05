def main():
    N = int(input())
    name_list = []
    for i in range(N):
        name_list.append(input())
    name_list.sort()
    for i in range(N-1):
        if name_list[i] == name_list[i+1]:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()