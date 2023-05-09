def main():
    s = input()
    t = "o" + "x" * 10 ** 5 + "o" + "x" * 10 ** 5 + "o"
    if s in t:
        print("Yes")
    else:
        print("No")
