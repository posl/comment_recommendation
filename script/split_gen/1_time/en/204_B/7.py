def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum([x-10 if x > 10 else 0 for x in a]))
