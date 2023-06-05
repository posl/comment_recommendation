def check(s):
    if(s.islower() or s.isupper() or len(s)%2!=0):
        return False
    else:
        return True
s=input()
if(check(s)):
    print("Yes")
else:
    print("No")

if __name__ == '__main__':
    check()