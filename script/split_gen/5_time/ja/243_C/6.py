def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    s = input()
    print(x)
    print(y)
    print(s)
    # x = [2, 1, 4]
    # y = [3, 1, 1]
    # s = "RRL"
    # x = [1, 2]
    # y = [1, 1]
    # s = "RR"
    # x = [1, 1, 0, 0, 0, 3, 2, 4, 4, 3]
    # y = [3, 4, 0, 2, 4, 1, 4, 2, 4, 3]
    # s = "RLRRRLRLRR"
    # x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # s = "RRRRRRRRRR"
    # x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # s = "LLLLLLLLLL"
    # x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # s = "RLRLRLRLRL"
    # x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # y = [1, 1, 1, 1, 1, 1, 1, 1,
