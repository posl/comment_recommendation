def main():
    #write your code here
    s1 = input()
    s2 = input()
    s3 = input()
    s = ["ABC", "ARC", "AGC", "AHC"]
    s.remove(s1)
    s.remove(s2)
    s.remove(s3)
    print(s[0])

if __name__ == '__main__':
    main()