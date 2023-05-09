def main():
    a, b = [int(x) for x in input().split()]
    print(max(a+b, a+a-1, b+b-1))
