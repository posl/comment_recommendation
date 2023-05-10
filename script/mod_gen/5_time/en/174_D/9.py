def main():
    N = int(input())
    c = input()
    c_list = list(c)
    c_list_left = []
    c_list_right = []
    for i in range(N):
        c_list_left.append(c_list[i])
        c_list_right.append(c_list[N-i-1])
    for i in range(N):
        if c_list_left[i] == 'R':
            break
    for j in range(N):
        if c_list_right[j] == 'W':
            break
    if i < j:
        print(j-i)
    else:
        print(0)

if __name__ == '__main__':
    main()