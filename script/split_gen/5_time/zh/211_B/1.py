def main():
    s = []
    for i in range(4):
        s.append(input())
    if "H" in s and "2B" in s and "3B" in s and "HR" in s:
        print("Yes")
    else:
        print("No")
