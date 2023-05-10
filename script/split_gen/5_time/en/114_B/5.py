def main():
    s = input()
    l = len(s)
    min = 999
    for i in range(l-2):
        x = int(s[i:i+3])
        if abs(x - 753) < min:
            min = abs(x - 753)
    print(min)
