def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    print(s1[int(t[0])-1] + s2[int(t[1])-1] + s3[int(t[2])-1] + s1[int(t[3])-1])

if __name__ == '__main__':
    main()