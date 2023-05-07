def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    print(len(set(s)))
