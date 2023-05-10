def main():
    n = input()
    n1 = n.replace("1", "x")
    n2 = n1.replace("9", "1")
    n3 = n2.replace("x", "9")
    print(n3)
