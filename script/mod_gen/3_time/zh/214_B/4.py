def main():
    s, t = map(int, input().split())
    count = 0
    for a in range(s+1):
        for b in range(s+1):
            for c in range(s+1):
                if a + b + c <= s and a * b * c <= t:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()