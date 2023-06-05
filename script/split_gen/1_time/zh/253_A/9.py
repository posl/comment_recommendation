def main():
    a,b,c = map(int,input().split())
    if b == sorted([a,b,c])[1]:
        print("是")
    else:
        print("没有")
