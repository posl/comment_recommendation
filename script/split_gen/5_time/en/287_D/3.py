def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        if s[:i] + t[i:] == t:
            print("Yes")
        else:
            print("No")
