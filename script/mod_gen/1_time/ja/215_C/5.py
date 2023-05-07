def main():
    s, k = input().split()
    k = int(k)
    s = list(s)
    s.sort()
    s = ''.join(s)
    print(s)
    count = 0
    while True:
        count += 1
        if count == k:
            break
        s = next_permutation(s)
        print(s)

if __name__ == '__main__':
    main()