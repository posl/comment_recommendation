def main():
    a,b = map(int,input().split())
    if(a > b):
        print(a - (a - b) // 2)
    else:
        print(b - (b - a) // 2)
