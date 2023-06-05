def main():
    s = input()
    t = input()
    if len(t) - len(s) == 1 and t[:len(s)] == s:
        print("Yes")
    else:
        print("No")
