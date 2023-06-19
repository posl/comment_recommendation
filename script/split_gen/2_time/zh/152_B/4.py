def main():
    a,b = map(int,input().split())
    a = str(a)
    b = str(b)
    a = a * int(b)
    b = b * int(a)
    print(min(a,b))
