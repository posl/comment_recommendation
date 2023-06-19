def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
n, q = map(int, input().split())
a = list(map(int, input().split()))
for i in range(q):
    k = int(input())
    l = []
    for j in range(1, 10 ** 18):
        if j not in a:
            l.append(j)
    print(l[k - 1])

if __name__ == '__main__':
    binary_search()