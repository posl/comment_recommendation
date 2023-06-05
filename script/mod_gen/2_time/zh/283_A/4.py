def main():
    n, m = map(int, input().split())
    #print(n, m)
    #print(type(n), type(m))
    #print(type(n), type(m))
    #print(type(n), type(m))
    i = 0
    j = 0
    list1 = []
    list2 = []
    while i < m:
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        list1.append(u)
        list2.append(v)
        i += 1
    #print(list1)
    #print(list2)
    i = 0
    j = 0
    list3 = []
    list4 = []
    while i < m:
        j = 0
        while j < m:
            if list1[i] != list1[j] and list1[i] != list2[j] and list2[i] != list1[j] and list2[i] != list2[j]:
                if list1[i] < list1[j]:
                    list3.append(list1[i])
                    list4.append(list1[j])
                elif list1[i] > list1[j]:
                    list3.append(list1[j])
                    list4.append(list1[i])
                if list1[i] < list2[j]:
                    list3.append(list1[i])
                    list4.append(list2[j])
                elif list1[i] > list2[j]:
                    list3.append(list2[j])
                    list4.append(list1[i])
                if list2[i] < list1[j]:
                    list3.append(list2[i])
                    list4.append(list1[j])
                elif list2[i] > list1[j]:
                    list3.append(list1[j])
                    list4.append(list2[i])
                if list2[i] < list2[j]:
                    list3.append(list2[i])
                    list4.append(list2[j])
                elif list2[i] > list2[j]:
                    list3.append(list2[j])
                    list4.append(list2[i])
            j += 1
        i += 1
    #print(list3)
    #print(list4)
    i = 0
    j = 0
    count = 0
    while i < len(list3):
        j = 0
        while j < len(list1):
            if list3[i]

if __name__ == '__main__':
    main()