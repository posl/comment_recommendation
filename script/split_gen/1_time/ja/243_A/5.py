def main():
    v,a,b,c = list(map(int,input().split()))
    if v <= a:
        print("F")
    elif v <= a+b:
        print("M")
    elif v <= a+b+c:
        print("T")
    return
