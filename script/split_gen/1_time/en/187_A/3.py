def main():
    a, b = [int(x) for x in input().split()]
    print(max(sum([int(x) for x in str(a)]), sum([int(x) for x in str(b)])))
