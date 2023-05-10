def main():
    N = int(input())
    count = 0
    for a in range(1, int(N**0.5)+1):
        for b in range(a, int(N**0.5)+1):
            if N % (a*b) == 0:
                if a == b:
                    count += 1
                else:
                    count += 3
    print(count)

if __name__ == '__main__':
    main()