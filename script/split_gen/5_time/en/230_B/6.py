def main():
    s = input()
    t = "o" + s + "o"
    print("Yes" if t.find("oo") != -1 else "No")
