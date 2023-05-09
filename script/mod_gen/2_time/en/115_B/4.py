def main():
    N = int(input())
    p_list = []
    for i in range(N):
        p_list.append(int(input()))
    p_list.sort(reverse = True)
    p_list[0] = int(p_list[0] / 2)
    print(sum(p_list))

if __name__ == '__main__':
    main()