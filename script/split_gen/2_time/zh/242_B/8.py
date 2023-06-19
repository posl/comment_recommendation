def problem242_b():
    string = input()
    list = []
    for i in range(len(string)):
        list.append(string[i])
    list.sort()
    for i in range(len(list)):
        print(list[i],end = "")
    print()
