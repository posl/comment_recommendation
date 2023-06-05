def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    S = ['ABC', 'ARC', 'AGC', 'AHC']
    for i in range(4):
        if S[i] not in s:
            print(S[i])
            break
