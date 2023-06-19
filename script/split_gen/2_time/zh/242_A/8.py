def main():
    a,b,c,x = map(int, input().split())
    if x <= a:
        print(1)
    elif a < x and x <= b:
        print(0.5)
    else:
        print(0)
