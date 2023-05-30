def main():
    N = int(input())
    used = set()
    for i in range(1, 2 * N + 2):
        print(i)
        used.add(i)
        a = int(input())
        used.add(a)
        if a == 0:
            return
    return
main()
