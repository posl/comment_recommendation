def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a < b:
        print(str(a)*b)
    else:
        print(str(b)*a)
