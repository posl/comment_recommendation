def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    s4 = ['ABC', 'ARC', 'AGC', 'AHC']
    for i in s4:
        if i not in s:
            print(i)
            break

if __name__ == '__main__':
    main()