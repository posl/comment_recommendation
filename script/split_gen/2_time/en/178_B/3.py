def main():
    a,b,c,d = map(int,input().split())
    if a * d > b * c:
        print(a * d)
    else:
        print(b * c)
