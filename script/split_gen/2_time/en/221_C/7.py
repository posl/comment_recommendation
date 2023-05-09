def main():
    n = int(input())
    if n < 10:
        print(0)
        return
    n = str(n)
    n = list(n)
    n.sort(reverse=True)
    n = ''.join(n)
    print(int(n[0]) * int(n[1]))
