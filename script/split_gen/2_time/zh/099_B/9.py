def main():
    a,b = map(int,input().split())
    print((b-a-1)*b//2 - a)
