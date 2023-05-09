def main():
    a,b = map(int,input().split())
    a = sum(map(int,str(a)))
    b = sum(map(int,str(b)))
    if a > b:
        print(a)
    else:
        print(b)
