def main():
    s1 = input()
    s2 = input()
    s3 = input()
    total = ["ABC", "ARC", "AGC", "AHC"]
    total.remove(s1)
    total.remove(s2)
    total.remove(s3)
    print(total[0])
