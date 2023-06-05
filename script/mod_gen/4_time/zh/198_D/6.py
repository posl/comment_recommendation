def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s3) < len(s1) or len(s3) < len(s2):
        print("UNSOLVABLE")
        exit()
    used = [False] * 10
    for c in s1 + s2 + s3:
        used[ord(c) - ord('a')] = True
    if sum(used) > 10:
        print("UNSOLVABLE")
        exit()
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    for i in range(10 ** len(s1)):
        n1 = str(i).zfill(len(s1))
        if any(n1[ord(c) - ord('a')] == '0' for c in s1):
            continue
        for j in range(10 ** len(s2)):
            n2 = str(j).zfill(len(s2))
            if any(n2[ord(c) - ord('a')] == '0' for c in s2):
                continue
            n3 = str(i + j).zfill(len(s3))
            if any(n3[ord(c) - ord('a')] == '0' for c in s3):
                continue
            if all(n1[ord(c) - ord('a')] == n2[ord(c) - ord('a')] == n3[ord(c) - ord('a')] for c in s1 + s2 + s3):
                print(i)
                print(j)
                print(i + j)
                exit()
    print("UNSOLVABLE")

if __name__ == '__main__':
    main()