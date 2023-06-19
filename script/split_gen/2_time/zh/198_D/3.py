def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > 10 or len(s2) > 10 or len(s3) > 10:
        print("UNSOLVABLE")
        return
    for i in range(10 ** (len(s1) - 1), 10 ** len(s1)):
        if len(set(str(i))) != len(set(s1)):
            continue
        for j in range(10 ** (len(s2) - 1), 10 ** len(s2)):
            if len(set(str(j))) != len(set(s2)):
                continue
            for k in range(10 ** (len(s3) - 1), 10 ** len(s3)):
                if len(set(str(k))) != len(set(s3)):
                    continue
                if i + j == k:
                    if isMatch(s1, str(i)) and isMatch(s2, str(j)) and isMatch(s3, str(k)):
                        print(i)
                        print(j)
                        print(k)
                        return
    print("UNSOLVABLE")
    return
