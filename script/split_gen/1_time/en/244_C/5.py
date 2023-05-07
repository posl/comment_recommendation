def main():
    n = int(input())
    a = set()
    b = set()
    for i in range(1, 2*n+2):
        print(i)
        a.add(i)
        b.add(int(input()))
        if 0 in b:
            break
        a.remove(i)
        b.remove(i)
        print(2*n+2-i)
        a.add(2*n+2-i)
        b.add(int(input()))
        if 0 in b:
            break
        a.remove(2*n+2-i)
        b.remove(2*n+2-i)
