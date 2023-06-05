def main():
    row = 2
    col = 2
    s1 = input()
    s2 = input()
    s1 = s1.replace('.', '')
    s2 = s2.replace('.', '')
    if len(s1) == 1 and len(s2) == 1:
        print("No")
    else:
        print("Yes")
