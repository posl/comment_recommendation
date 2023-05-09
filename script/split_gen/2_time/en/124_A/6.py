def main():
    a, b = map(int, input().split())
    print(max(a+b, a+b-1, a-1+b, a-1+b-1))
