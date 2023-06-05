def main():
    n = int(input())
    s_p_list = []
    for i in range(n):
        s, p = input().split()
        s_p_list.append((s, int(p)))
    s_p_list.sort(key=lambda x: x[0])
    s_p_list.sort(key=lambda x: x[1], reverse=True)
    for i in range(n):
        print(i + 1)

if __name__ == '__main__':
    main()