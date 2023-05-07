def main():
    s = input()
    t = "o" * (10 ** 5) + "x" * (10 ** 5) + "o" * (10 ** 5)
    if s in t:
        print("Yes")
    else:
        print("No")
