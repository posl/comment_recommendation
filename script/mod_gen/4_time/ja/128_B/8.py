def sort_list(list):
    list.sort(key=lambda x: x[1], reverse=True)
    return list
N = int(input())
list = []
for i in range(N):
    S, P = input().split()
    P = int(P)
    list.append([S, P, i+1])
list = sort_list(list)
list = sort_list(list)
for i in range(N):
    print(list[i][2])

if __name__ == '__main__':
    sort_list()