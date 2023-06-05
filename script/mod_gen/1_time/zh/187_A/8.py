def solution():
    a, b = map(int, input().split())
    a = sum(map(int, list(str(a))))
    b = sum(map(int, list(str(b))))
    print(max(a, b))

if __name__ == '__main__':
    solution()