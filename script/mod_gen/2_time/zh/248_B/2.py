def solve():
    s = input()
    num_dict = {}
    for i in range(10):
        num_dict[str(i)] = 0
    for i in s:
        num_dict[i] += 1
    for i in range(10):
        if num_dict[str(i)] == 0:
            print(i)
            break

if __name__ == '__main__':
    solve()