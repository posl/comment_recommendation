def main():
    a,b = map(int,input().split())
    if a > b:
        print(a+(a-1))
    elif a < b:
        print(b+(b-1))
    else:
        print(a+b)
