def main():
    a, b, c, d, e = map(int, input().split())
    nums = [a, b, c, d, e]
    print(len(set(nums)))
