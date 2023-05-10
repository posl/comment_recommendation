def main():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    b = []
    c = []
    for i in range(q):
        b_c = list(map(int,input().split()))
        b.append(b_c[0])
        c.append(b_c[1])
    b_set = set(b)
    b_list = list(b_set)
    b_list.sort()
    b_list.reverse()
    b_list.append(0)
    c_list = []
    for i in range(len(b_list)-1):
        c_list.append(0)
    for i in range(len(b_list)-1):
        for j in range(len(b)):
            if b_list[i] == b[j]:
                c_list[i] += c[j]
    #print(b_list)
    #print(c_list)
    #print(a)
    #print("")
    for i in range(len(a)):
        for j in range(len(b_list)-1):
            if a[i] == b_list[j]:
                a[i] = c_list[j]
    for i in range(len(a)):
        print(a[i],end=" ")

if __name__ == '__main__':
    main()