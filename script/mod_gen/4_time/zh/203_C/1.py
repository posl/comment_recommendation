def main():
    n, k = map(int, input().split())
    array = []
    for i in range(n):
        a, b = map(int, input().split())
        array.append((a, b))
    array.sort()
    money = k
    for i in range(n):
        if money >= array[i][0]:
            money += array[i][1]
    print(money)
main()
