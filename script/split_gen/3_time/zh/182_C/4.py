def main():
    n = int(input())
    if n % 3 == 0:
        print(0)
        return
    n = str(n)
    for i in range(len(n)):
        if (int(n) - int(n[i])) % 3 == 0 and len(n) > 1:
            print(1)
            return
    if len(n) > 2:
        print(2)
    else:
        print(-1)
