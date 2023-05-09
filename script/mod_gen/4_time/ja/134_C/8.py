def main():
    n = int(input())
    a_list = []
    for i in range(n):
        a_list.append(int(input()))
    max_a = max(a_list)
    max_a2 = sorted(a_list)[-2]
    for i in range(n):
        if a_list[i] != max_a:
            print(max_a)
        else:
            print(max_a2)

if __name__ == '__main__':
    main()