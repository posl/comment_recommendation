def solve():
    w = int(input())
    if w <= 2:
        print(2)
        print(1, 1)
    else:
        print(w)
        if w % 2 == 0:
            for i in range(w//2):
                print(2, end=' ')
        else:
            for i in range(w//2-1):
                print(2, end=' ')
            print(3)
solve()

if __name__ == '__main__':
    solve()