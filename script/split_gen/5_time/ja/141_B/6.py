def main():
    s = input()
    l = len(s)
    for i in range(l):
        if i % 2 == 0:
            if s[i] == "L":
                print("No")
                exit()
        else:
            if s[i] == "R":
                print("No")
                exit()
    print("Yes")
