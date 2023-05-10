def star():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    a_set = set(a)
    b_set = set(b)
    if len(a_set) == 1 or len(b_set) == 1:
        print("Yes")
    else:
        print("No")
star()

if __name__ == '__main__':
    star()