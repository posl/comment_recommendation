def main():
    a,b = map(int,input().split())
    if b % a == 0:
        print(int(b/a)-1)
    else:
        print(int(b/a))
