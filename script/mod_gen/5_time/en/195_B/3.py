def solve(a, b, w):
    min_oranges = 0
    max_oranges = 0
    for i in range(1, 1001):
        if a*i <= w*1000 <= b*i:
            if min_oranges == 0:
                min_oranges = i
            max_oranges = i
    if min_oranges == 0:
        print("UNSATISFIABLE")
    else:
        print(min_oranges, max_oranges)

if __name__ == '__main__':
    solve()