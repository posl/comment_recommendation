def main():
    s = input()
    min_diff = 999
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        diff = abs(x-753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
