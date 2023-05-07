def main():
    c1, c2, c3 = input().rstrip().split()
    if c1 == c2 == c3:
        print("Won")
    else:
        print("Lost")
