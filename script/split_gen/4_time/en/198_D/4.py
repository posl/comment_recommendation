def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s2):
        if len(s1) > len(s3):
            max_len = len(s1)
        else:
            max_len = len(s3)
    else:
        if len(s2) > len(s3):
            max_len = len(s2)
        else:
            max_len = len(s3)
    for i in range(10 ** (max_len - 1), 10 ** max_len):
        n1 = str(i)
        n2 = str(i)
        n3 = str(i)
        for j in range(len(n1), max_len):
            n1 = "0" + n1
        for j in range(len(n2), max_len):
            n2 = "0" + n2
        for j in range(len(n3), max_len):
            n3 = "0" + n3
        for j in range(max_len):
            if s1[j] == s2[j] and s1[j] != s3[j]:
                break
            if s1[j] == s3[j] and s1[j] != s2[j]:
                break
            if s2[j] == s3[j] and s1[j] != s2[j]:
                break
            if s1[j] == s2[j] and s1[j] == s3[j]:
                if n1[j] != n2[j]:
                    break
                elif n1[j] != n3[j]:
                    break
                elif n2[j] != n3[j]:
                    break
            if s1[j] != s2[j] and s1[j] != s3[j] and s2[j] != s3[j]:
                if n1[j] == n2[j] or n1[j] == n3[j] or n2[j] == n3[j]:
                    break
        else:
            if int(n1) + int(n2) == int(n3):
                print(n1)
                print(n2)
                print(n3)
                exit()
    print("UNSOLVABLE")
