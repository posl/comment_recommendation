def main():
    a,b,c = map(int, input().split())
    print(c - (a - b) if c >= (a - b) else c)
