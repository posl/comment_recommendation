def main():
    s1 = input()
    s2 = input()
    s3 = input()
    print("".join(set(["ABC","ARC","AGC","AHC"]) - set([s1,s2,s3])))

if __name__ == '__main__':
    main()