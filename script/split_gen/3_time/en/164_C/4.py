def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = set(s)
    print(len(s))
