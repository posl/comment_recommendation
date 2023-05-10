def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_set = set(a)
    a_dict = {}
    for i in a_set:
        a_dict[i] = a.count(i)
    a_dict = sorted(a_dict.items(), key=lambda x:x[1], reverse=True)
    if len(a) == 1:
        print(0)
    elif len(a) == 2:
        if a[0] == a[1]:
            print(0)
        else:
            print(1)
    elif len(a_set) == 1:
        print(0)
    else:
        if a_dict[0][1] == 1:
            print(1)
        else:
            if a_dict[0][1] == 2:
                if a_dict[1][1] == 1:
                    print(1)
                else:
                    print(2)
            else:
                if a_dict[1][1] == 1:
                    print(2)
                else:
                    print(3)

if __name__ == '__main__':
    main()