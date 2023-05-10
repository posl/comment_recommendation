def solve():
    v, a, b, c = map(int, input().split())
    if a >= v:
        print("F")
    elif a < v and b >= (v - a):
        print("M")
    elif a < v and b < (v - a) and c >= (v - a - b):
        print("T")
    else:
        print("T")

if __name__ == '__main__':
    solve()