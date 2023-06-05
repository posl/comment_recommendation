def main():
    k = int(input())
    s = ''
    for i in range(k):
        s += chr(ord('A')+i)
    print(s)
