def main():
    n = int(input())
    a = set()
    for i in range(1, 2*n+2):
        print(i)
        a.add(int(input()))
        if len(a) == 2*n+1:
            break
