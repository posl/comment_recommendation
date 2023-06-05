def main():
    s = input()
    ls = s.split()
    for i in range(26):
        ls[i] = int(ls[i])
    for i in range(26):
        print(chr(ls[i]+96),end='')
    print()
