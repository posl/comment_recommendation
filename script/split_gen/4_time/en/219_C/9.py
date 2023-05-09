def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    y = sorted(s, key=lambda x: [x[i] for i in range(len(x))])
    for i in range(n):
        print(y[i])
