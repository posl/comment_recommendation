def solution():
    N = int(input())
    name = input()
    name_list = []
    name_list.append(name)
    for i in range(1, N):
        name = input()
        name_list.append(name)
    print(max(name_list, key=name_list.count))

if __name__ == '__main__':
    solution()