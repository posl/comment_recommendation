def solution():
    a, b = map(int, input().split())
    if a > b:
        print(0)
    else:
        print(b - a + 1)
solution()

if __name__ == '__main__':
    solution()