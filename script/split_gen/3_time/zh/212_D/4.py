def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    a = a[::-1]
    bag = []
    for i in range(n):
        if a[i][0] == 1:
            bag.append(a[i][1])
        elif a[i][0] == 2:
            bag = [x+a[i][1] for x in bag]
        else:
            print(min(bag))
            bag.remove(min(bag))
