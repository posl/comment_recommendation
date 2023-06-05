def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=lambda x: [x[y] for y in range(len(x))])
    print('\n'.join(s))
