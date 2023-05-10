def main():
    n = int(input())
    s = input()
    l = len(s)
    result = ""
    for i in range(l):
        result += chr((ord(s[i]) - 65 + n) % 26 + 65)
    print(result)
