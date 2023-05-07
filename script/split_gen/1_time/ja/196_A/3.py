def main():
    a,b = map(int, input().split())
    c,d = map(int, input().split())
    print(max([b-d, b-c, a-d, a-c]))
