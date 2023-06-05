def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s3) < len(s1) or len(s3) < len(s2):
        print("UNSOLVABLE")
        return
    s1 = list(s1)
    s2 = list(s2)
    s3 = list(s3)
    s1.reverse()
    s2.reverse()
    s3.reverse()
    # print(s1, s2, s3)
    s1 = list(map(ord, s1))
    s2 = list(map(ord, s2))
    s3 = list(map(ord, s3))
    # print(s1, s2, s3)
    for i in range(0, 26):
        s1 = list(map(lambda x: x-ord('a'), s1))
        s2 = list(map(lambda x: x-ord('a'), s2))
        s3 = list(map(lambda x: x-ord('a'), s3))
        # print(s1, s2, s3)
        for j in range(0, 26):
            s1 = list(map(lambda x: (x+1)%26, s1))
            s2 = list(map(lambda x: (x+1)%26, s2))
            s3 = list(map(lambda x: (x+1)%26, s3))
            # print(s1, s2, s3)
            if s1[-1] + s2[-1] == s3[-1]:
                s1 = list(map(lambda x: x+ord('a'), s1))
                s2 = list(map(lambda x: x+ord('a'), s2))
                s3 = list(map(lambda x: x+ord('a'), s3))
                s1.reverse()
                s2.reverse()
                s3.reverse()
                for i in range(0, len(s1)):
                    print(s1[i], end="")
                print()
                for i in range(0, len(s2)):
                    print(s2[i], end="")
                print()
                for i in range(0, len(s3)):
                    print(s3[i], end="")
                print()
                return
        s1 = list(map(lambda x: x+ord('a'), s1))
        s2 = list(map(lambda x: x+ord('a'), s2

if __name__ == '__main__':
    main()