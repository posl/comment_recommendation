def main():
    s = input()
    t = input()
    if len(set(s)) == len(set(t)) == 26:
        print("Yes")
    else:
        print("No")
