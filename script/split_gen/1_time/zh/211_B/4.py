def main():
    a = []
    for i in range(4):
        a.append(input())
    if "H" in a and "2B" in a and "3B" in a and "HR" in a:
        print("Yes")
    else:
        print("No")
