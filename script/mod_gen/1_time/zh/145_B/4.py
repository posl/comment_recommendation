def is_double_copy(s):
    if len(s)%2!=0:
        return False
    else:
        l=len(s)//2
        return s[:l]==s[l:]
n=int(input())
s=input()

if __name__ == '__main__':
    is_double_copy()