def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    max_a = max(a_list)
    max_a_index = a_list.index(max_a)
    for i in range(n):
        if i == max_a_index:
            print(max(a_list[:max_a_index] + a_list[max_a_index+1:]))
        else:
            print(max_a)

if __name__ == '__main__':
    main()