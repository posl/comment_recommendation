def main():
    s = input()
    s = s[::-1]
    s = s.replace("0", "a")
    s = s.replace("1", "b")
    s = s.replace("6", "0")
    s = s.replace("8", "1")
    s = s.replace("9", "6")
    s = s.replace("a", "9")
    s = s.replace("b", "8")
    print(s)
