def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) == len(s2) == len(s3) == 1:
        if s3 == chr(ord(s1) + ord(s2) - ord('a')):
            print(1)
            print(1)
            print(2)
        else:
            print("UNSOLVABLE")
        return
    if len(s1) == len(s2) == 1:
        if s1 == s2 and s2 != s3:
            print("UNSOLVABLE")
            return
        if s3 == chr(ord(s1) + ord(s2) - ord('a')):
            print(1)
            print(1)
            print(2)
        else:
            print("UNSOLVABLE")
        return
    if len(s1) == 1 and len(s2) == 2:
        if s3[0] == chr(ord(s1) + ord(s2[0]) - ord('a')):
            print(1)
            print(1)
            print(2)
        else:
            print("UNSOLVABLE")
        return
    if len(s1) == 1 and len(s2) == 3:
        if s3[0] == chr(ord(s1) + ord(s2[0]) - ord('a')):
            print(1)
            print(1)
            print(2)
        else:
            print("UNSOLVABLE")
        return
    if len(s1) == 2 and len(s2) == 2:
        if s1[0] == s2[0] and s3[0] != s3[1]:
            print("UNSOLVABLE")
            return
        if s1[0] == s2[0] and s3[0] == s3[1]:
            print(1)
            print(1)
            print(2)
            return
        if s1[0] == s

if __name__ == '__main__':
    solve()