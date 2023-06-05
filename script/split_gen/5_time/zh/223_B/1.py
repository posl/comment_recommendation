def main():
    s = input()
    min = s
    max = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s > max:
            max = s
        if s < min:
            min = s
    print(min)
    print(max)
