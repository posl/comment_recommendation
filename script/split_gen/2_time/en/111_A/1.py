def main():
    n = input()
    n = n.replace("1", "x")
    n = n.replace("9", "1")
    n = n.replace("x", "9")
    print(n)
