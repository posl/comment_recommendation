def main():
    a, b = map(int, input().split())
    print(max(a+b-1, a+b, a+b+1))
