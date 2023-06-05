def main():
    a = input()
    b = a.split()
    b.sort()
    if (int(b[1]) - int(b[0])) == (int(b[2]) - int(b[1])):
        print("Yes")
    else:
        print("No")
