def solve():
    n = int(input())
    candidates = {}
    for i in range(n):
        name = input()
        if name in candidates:
            candidates[name] += 1
        else:
            candidates[name] = 1
    print(max(candidates, key=candidates.get))
