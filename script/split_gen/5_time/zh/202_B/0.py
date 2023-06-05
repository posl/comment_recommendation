def main():
    s = input()
    s = s[::-1]
    s = s.replace("6", "x")
    s = s.replace("9", "6")
    s = s.replace("x", "9")
    s = s.replace("1", "x")
    s = s.replace("0", "1")
    s = s.replace("x", "0")
    print(s)
