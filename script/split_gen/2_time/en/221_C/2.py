def main():
    n = input()
    l = len(n)
    if l == 2:
        print(max(int(n[0])*int(n[1]), int(n[1])*int(n[0])))
    else:
        print(max(int(n[0])*(int(''.join(n[1:]))), (int(''.join(n[:l-1])))*(int(n[l-1]))))
