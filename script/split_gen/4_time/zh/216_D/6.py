def main():
    N,M = map(int,input().split())
    k_list = []
    a_list = []
    for i in range(M):
        k_list.append(int(input()))
        a_list.append(list(map(int,input().split())))
    print(N,M,k_list,a_list)
    print(a_list[0][1])
    print(a_list[1][1])
    if a_list[0][1] == a_list[1][1]:
        print("Yes")
    else:
        print("No")
main()
