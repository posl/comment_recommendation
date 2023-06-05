def main():
    a,b = map(int,input().split())
    if a < b:
        for i in range(b):
            print(a,end='')
    else:
        for i in range(a):
            print(b,end='')
    print()
