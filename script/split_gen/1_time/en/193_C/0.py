def main():
    n = int(input())
    print(n - len(set([a ** b for a in range(2, int(n ** 0.5) + 1) for b in range(2, int(n ** 0.5) + 1)])))
main()
