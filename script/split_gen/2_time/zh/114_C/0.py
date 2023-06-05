def main():
    s = input()
    min_diff = 1000
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        if abs(x-753) < min_diff:
            min_diff = abs(x-753)
    print(min_diff)
main()
