def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a == b:
        print("IMPOSIBLE")
    else:
        print(int((a+b)/2))
