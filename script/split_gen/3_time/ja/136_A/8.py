def main():
    a,b,c = map(int,input().split())
    print(c if a >= c else a - (c - b))
