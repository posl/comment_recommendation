def main():
    a,b,c = map(int, input().split())
    print(max(a+b, a+c, b+c))
