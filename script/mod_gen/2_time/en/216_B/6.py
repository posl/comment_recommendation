def main():
    N = int(input())
    name_list = []
    for i in range(N):
        name_list.append(input().split())
    for i in range(N):
        for j in range(N):
            if i != j:
                if name_list[i][0] == name_list[j][0] and name_list[i][1] == name_list[j][1]:
                    print('Yes')
                    return
    print('No')
    return

if __name__ == '__main__':
    main()