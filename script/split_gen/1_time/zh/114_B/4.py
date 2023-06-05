def main():
    s = input()
    min = 999
    for i in range(len(s)-2):
        a = int(s[i:i+3])
        if abs(a-753) < min:
            min = abs(a-753)
    print(min)
