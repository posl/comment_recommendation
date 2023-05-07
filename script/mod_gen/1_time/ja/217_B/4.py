def main():
    S = [input() for _ in range(3)]
    for s in ['ABC', 'ARC', 'AGC', 'AHC']:
        if s not in S:
            print(s)
            break

if __name__ == '__main__':
    main()