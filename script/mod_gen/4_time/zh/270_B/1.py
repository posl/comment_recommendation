def solution():
    x, y, z = map(int, input().split())
    if x < y:
        print(-1)
    else:
        print(x + y + z)

if __name__ == '__main__':
    solution()