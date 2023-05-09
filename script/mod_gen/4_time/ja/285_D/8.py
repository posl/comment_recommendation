def main():
    n = int(input())
    s_t_list = []
    for _ in range(n):
        s_t_list.append(input().split())
    s_t_list.sort(key=lambda x: x[1])
    s_list = [s_t[0] for s_t in s_t_list]
    t_list = [s_t[1] for s_t in s_t_list]
    for i in range(n-1):
        if t_list[i] == t_list[i+1]:
            print("No")
            return
    for i in range(n-1):
        if s_list[i] == s_list[i+1]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()