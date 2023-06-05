def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    l = ['ABC', 'ARC', 'AGC', 'AHC']
    for i in range(4):
        if l[i] not in s:
            print(l[i])
            break

if __name__ == '__main__':
    main()