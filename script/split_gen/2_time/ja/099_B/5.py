def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a == b:
        print(0)
    else:
        print(b-a-1)
