def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = [S1, S2, S3]
    for i in ["ABC", "ARC", "AGC", "AHC"]:
        if i not in S:
            print(i)
