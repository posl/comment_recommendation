def main():
    a,b = map(int, input().split())
    k = (a+b)/2
    if k.is_integer():
        print(int(k))
    else:
        print("IMPOSSIBLE")
