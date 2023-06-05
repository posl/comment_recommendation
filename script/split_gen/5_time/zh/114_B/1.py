def main():
    s = input()
    n = len(s)
    x = 753
    for i in range(n-2):
        x = min(x, abs(753-int(s[i:i+3])))
    print(x)
