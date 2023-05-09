def main():
    s = input()
    x = 753
    for i in range(len(s)-2):
        x = min(x,abs(753-int(s[i:i+3])))
    print(x)
