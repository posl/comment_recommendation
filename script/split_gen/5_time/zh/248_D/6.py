def get_input():
    num = int(input())
    list1 = input().split()
    list1 = [int(x) for x in list1]
    num2 = int(input())
    list2 = []
    for i in range(num2):
        list3 = input().split()
        list3 = [int(x) for x in list3]
        list2.append(list3)
    return num, list1, num2, list2
