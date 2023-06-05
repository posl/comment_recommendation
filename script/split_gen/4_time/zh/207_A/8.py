def main():
    a,b,c = map(int,input().split())
    max = a+b+c
    if max < a+b:
        max = a+b
    if max < a+c:
        max = a+c
    if max < b+c:
        max = b+c
    print(max)
