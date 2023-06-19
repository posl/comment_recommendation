def main():
    a, b = map(int, input().split())
    print(max(sum([int(x) for x in str(a)]), sum([int(x) for x in str(b)])))
