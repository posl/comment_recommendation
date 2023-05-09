def main():
    n = int(input())
    a_list = []
    b_list = []
    for i in range(n):
        a,b = map(int,input().split())
        a_list.append(a)
        b_list.append(b)
    a_min = min(a_list)
    b_min = min(b_list)
    a_min_index = a_list.index(a_min)
    b_min_index = b_list.index(b_min)
    if a_min_index == b_min_index:
        a_list.pop(a_min_index)
        b_list.pop(b_min_index)
        a_min2 = min(a_list)
        b_min2 = min(b_list)
        print(min(a_min+b_min2,a_min2+b_min))
    else:
        print(max(a_min,b_min))

if __name__ == '__main__':
    main()