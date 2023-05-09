def main():
    s = input()
    t = input()
    ls = len(s)
    lt = len(t)
    for i in range(lt+1):
        if s[i:i+lt] == t:
            print("Yes")
        else:
            print("No")
