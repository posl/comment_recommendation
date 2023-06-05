def problem167_a():
    s = input()
    t = input()
    if s + t[-1] == t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    problem167_a()