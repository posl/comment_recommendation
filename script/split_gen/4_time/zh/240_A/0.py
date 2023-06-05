def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if b-a == 1 or b-a == -1 or b-a == 9:
        print('Yes')
    else:
        print('No')
