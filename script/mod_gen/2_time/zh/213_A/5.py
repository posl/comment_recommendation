def main():
    n = int(input())
    list = []
    for i in range(n):
        list.append(input())
    for i in range(n):
        if list[i][0] == '1':
            list[i] = list[i].split()
            list[i] = int(list[i][1])
        elif list[i][0] == '2':
            list[i] = list[i].split()
            list[i] = int(list[i][1])
        else:
            list[i] = int(list[i])
    list1 = []
    for i in range(n):
        if list[i] == 3:
            list1.append(i)
    list2 = []
    for i in range(len(list1)):
        for j in range(list1[i]):
            if list[j] == 3:
                list2.append(j)
    list3 = []
    for i in range(len(list2)):
        list4 = []
        for j in range(list2[i], list1[i]):
            list4.append(list[j])
        list3.append(list4)
    list5 = []
    for i in range(len(list3)):
        list5.append(min(list3[i]))
    for i in range(len(list5)):
        print(list5[i])

if __name__ == '__main__':
    main()