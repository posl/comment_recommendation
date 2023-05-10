def main():
    n, k = map(int, input().split())
    p_list = []
    for i in range(n):
        p_list.append(list(map(int, input().split())))
    for i in range(n):
        if sum(p_list[i]) < k * 3:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()