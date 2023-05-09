def main():
    s = input()
    min = 999
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        if abs(x - 753) < min:
            min = abs(x - 753)
    print(min)
