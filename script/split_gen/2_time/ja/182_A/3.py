def main():
    a,b = map(int,input().split())
    if a*2+100 <= b:
        print(0)
    else:
        print(a*2+100-b)
