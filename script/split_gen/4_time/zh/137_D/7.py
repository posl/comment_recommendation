def main():
    n, m = map(int, input().split())
    works = []
    for i in range(n):
        a, b = map(int, input().split())
        works.append([a, b])
    works.sort(key=lambda x: x[0])
    sum = 0
    day = 0
    index = 0
    while day < m:
        if index < n and works[index][0] == day + 1:
            sum += works[index][1]
            index += 1
        day += 1
    print(sum)
