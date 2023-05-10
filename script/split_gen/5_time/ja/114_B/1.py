def main():
    s = input()
    min_dif = 753
    for i in range(len(s) - 2):
        dif = abs(int(s[i:i+3]) - 753)
        if dif < min_dif:
            min_dif = dif
    print(min_dif)
