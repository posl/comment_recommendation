def replace_list(list, b, c):
    for i in range(len(list)):
        if list[i] == b:
            list[i] = c
    return list
n = int(input())
a = list(map(int, input().split()))
q = int(input())
bc = [list(map(int, input().split())) for i in range(q)]
for i in range(q):
    a = replace_list(a, bc[i][0], bc[i][1])
    print(sum(a))

if __name__ == '__main__':
    replace_list()