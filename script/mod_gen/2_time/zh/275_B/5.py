def problem275_a():
    n = int(input())
    heights = list(map(int, input().split()))
    print(heights.index(max(heights)) + 1)
problem275_a()
