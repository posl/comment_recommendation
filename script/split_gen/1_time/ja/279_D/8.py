def main():
    import math
    a,b = map(int, input().split())
    if a<b:
        print(a)
    else:
        print(math.sqrt(2*a/b))
