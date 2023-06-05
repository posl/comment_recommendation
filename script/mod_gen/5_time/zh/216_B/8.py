def main():
    N = int(input())
    name_list = []
    for i in range(N):
        name_list.append(input())
    for i in range(N):
        for j in range(i+1,N):
            if name_list[i] == name_list[j]:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()