def main():
    s = input()
    if s.count("A") == 1 and s.count("B") == 2:
        print("Yes")
    elif s.count("A") == 2 and s.count("B") == 1:
        print("Yes")
    else:
        print("No")
