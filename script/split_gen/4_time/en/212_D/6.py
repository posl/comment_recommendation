def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    a.reverse()
    bag = []
    for i in range(n):
        if a[i][0] == 1:
            bag.append(a[i][1])
        elif a[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += a[i][1]
        elif a[i][0] == 3:
            bag.sort()
            print(bag.pop(0))
    return 0
