def main():
    s,k = input().split()
    k = int(k)
    s = list(s)
    s.sort()
    s = ''.join(s)
    result = ''
    for i in range(k):
        result = next_permutation(s)
    print(result)

if __name__ == '__main__':
    main()