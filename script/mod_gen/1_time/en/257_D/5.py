def get_input():
    N = int(input())
    trampolines = []
    for i in range(N):
        x, y, p = map(int, input().split())
        trampolines.append((x, y, p))
    return N, trampolines

if __name__ == '__main__':
    get_input()