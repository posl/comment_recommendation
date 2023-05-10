def get_parent(i):
    if i == 1:
        return 0
    else:
        return get_parent(i // 2) + 1
n = int(input())
a = list(map(int, input().split()))
for i in range(1, 2 ** n + 1):
    print(get_parent(i))

if __name__ == '__main__':
    get_parent()