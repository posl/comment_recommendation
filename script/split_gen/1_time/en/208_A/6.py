def main():
    a,b = map(int, input().split())
    if 6*a < b:
        print("No")
    elif b < a:
        print("No")
    else:
        print("Yes")
