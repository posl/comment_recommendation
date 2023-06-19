def main():
    n = int(input())
    s = input()
    s2 = ""
    for i in s:
        if ord(i)+n > 90:
            s2 += chr(ord(i)+n-26)
        else:
            s2 += chr(ord(i)+n)
    print(s2)
