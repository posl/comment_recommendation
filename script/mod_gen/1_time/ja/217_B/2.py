def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = ["ABC","ARC","AGC","AHC"]
    s4.remove(s1)
    s4.remove(s2)
    s4.remove(s3)
    print(s4[0])

if __name__ == '__main__':
    main()