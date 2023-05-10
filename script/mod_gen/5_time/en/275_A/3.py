def max_height_bridge():
    n = int(input())
    h = list(map(int, input().split()))
    return h.index(max(h)) + 1

if __name__ == '__main__':
    max_height_bridge()