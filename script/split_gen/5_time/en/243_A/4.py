def main():
    v,a,b,c = map(int, input().split())
    if a >= v:
        print("F")
    elif a+b >= v:
        print("M")
    else:
        print("T")
