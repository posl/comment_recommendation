def main():
    s = input()
    t = "o" + s + "o"
    print("Yes" if t.find("o"*7) > -1 else "No")
