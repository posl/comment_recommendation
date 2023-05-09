def main():
    s = input()
    t = "o" + "x" * 10 ** 5
    t = t * 10 ** 5
    if s in t:
        print("Yes")
    else:
        print("No")
