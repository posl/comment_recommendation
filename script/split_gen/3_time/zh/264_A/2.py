def main():
    str1 = 'atcoder'
    str2 = input().split()
    L = int(str2[0])
    R = int(str2[1])
    print(str1[L-1:R])
