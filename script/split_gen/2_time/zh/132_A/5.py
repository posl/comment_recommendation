def main():
    s = input()
    if len(s) != 4:
        print("No")
        return
    if len(set(s)) == 2:
        print("Yes")
    else:
        print("No")
