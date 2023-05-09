def main():
    #n = int(input())
    #a, b = map(int, input().split())
    #c = list(map(int, input().split()))
    #s = input()
    s = input()
    s1 = sorted(s)
    s2 = sorted(set(s))
    if len(s1) == len(s2) and s1[0].isupper() and s1[0] != s2[0]:
        print('Yes')
    else:
        print('No')
