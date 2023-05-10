def main():
    n = int(input())
    s = input()
    for i in range(n):
        if s[i] == "," and i%2 == 1:
            print(".", end="")
        else:
            print(s[i], end="")
    print()
