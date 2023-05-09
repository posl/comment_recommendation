def main():
    a,b = map(int, input().split())
    a = sum([int(i) for i in str(a)])
    b = sum([int(i) for i in str(b)])
    print(max(a,b))
