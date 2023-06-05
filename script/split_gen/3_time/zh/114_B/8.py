def main():
    s = input()
    sub = 1000
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        sub = min(sub,abs(753-x))
    print(sub)
