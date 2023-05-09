def main():
    a,b = [int(x) for x in input().split()]
    print(a*b - (a+b) + 1)
