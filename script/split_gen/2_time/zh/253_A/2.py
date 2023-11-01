def main():
    a,b,c = map(int,input().split())
    if a <= 100 and b <= 100 and c <= 100:
        if a <= b <= c or c <= b <= a:
