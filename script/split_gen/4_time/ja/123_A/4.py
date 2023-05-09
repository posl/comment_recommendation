def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if (b - a) > k:
        print(":(")
        return
    if (c - b) > k:
        print(":(")
        return
    if (d - c) > k:
        print(":(")
        return
    if (e - d) > k:
        print(":(")
        return
    print("Yay!")
