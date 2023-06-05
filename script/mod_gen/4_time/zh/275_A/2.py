def problems275_a():
    n = int(input())
    heights = list(map(int, input().split()))
    print(heights.index(max(heights)) + 1)

if __name__ == '__main__':
    problems275_a()