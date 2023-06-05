def main():
    a = input()
    b = a.split()
    b.sort()
    if b[0] == b[1] and b[1] != b[2] and b[2] == b[3] and b[3] == b[4]:
        print("Yes")
    else:
        print("No")
