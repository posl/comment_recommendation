def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=lambda x: [x.translate(str.maketrans(x,x[::-1])),x])
    for i in range(n):
        print(s[i])
