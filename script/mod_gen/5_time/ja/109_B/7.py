def main():
    N = int(input())
    W_list = []
    for i in range(N):
        W_list.append(input())
    flag = True
    for i in range(N-1):
        if W_list[i] in W_list[i+1:]:
            flag = False
            break
        if W_list[i][-1] != W_list[i+1][0]:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()