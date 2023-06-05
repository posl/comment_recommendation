def main():
    s1 = input()
    s2 = input()
    s3 = input()
    l = ['ABC', 'ARC', 'AGC', 'AHC']
    l.remove(s1)
    l.remove(s2)
    l.remove(s3)
    print(l[0])

if __name__ == '__main__':
    main()