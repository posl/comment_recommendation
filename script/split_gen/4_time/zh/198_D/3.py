def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s2) or len(s1) > len(s3) or len(s2) > len(s3):
        print("UNSOLVABLE")
        return
    else:
        for i in range(10**(len(s3)-len(s1)), 10**(len(s3)-len(s1)+1)):
            if len(str(i)) != len(s1):
                continue
            else:
                if is_valid(s1, s2, s3, i):
                    print(i)
                    print(i*(10**(len(s3)-len(s2))))
                    print(int(s3))
                    return
        print("UNSOLVABLE")
        return
