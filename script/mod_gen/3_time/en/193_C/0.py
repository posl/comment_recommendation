def main():
    N = int(input())
    print(N - len(set([a**b for a in range(2, int(N**0.5)+1) for b in range(2, int(N**0.5)+1)])))

if __name__ == '__main__':
    main()