def main():
    s = input()
    t = "o" * (len(s) // 2) + "x" * (len(s) // 2)
    if len(s) % 2 == 1:
        t = t + "o"
    if s == t:
        print("Yes")
    else:
        print("No")
