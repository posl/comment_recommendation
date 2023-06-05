def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p_list = list(map(int, input().split()))
    p_list.sort()
    if x not in p_list:
        print(x)
        return
    for i in range(1, 101):
        if x - i not in p_list:
            print(x - i)
            return
        elif x + i not in p_list:
            print(x + i)
            return
    return

if __name__ == '__main__':
    main()