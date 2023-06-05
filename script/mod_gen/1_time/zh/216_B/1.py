def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input())
    name_list.sort()
    for i in range(n-1):
        if name_list[i] == name_list[i+1]:
            print('Yes')
            return
    print('No')
main()
