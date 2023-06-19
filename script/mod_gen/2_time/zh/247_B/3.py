def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input().split())
    for i in range(n):
        for j in range(i+1,n):
            if name_list[i][0] == name_list[j][0] or name_list[i][1] == name_list[j][1]:
                print("Yes")
                return
    print("No")
main()
