def main():
    s = input()
    s = s[::-1]
    for i, c in enumerate(s):
        if c == 'a':
            print(len(s) - i)
            return
    print('-1')
