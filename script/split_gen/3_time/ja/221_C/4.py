def main():
    n = input()
    n = list(n)
    n.sort(reverse=True)
    a = n[0]
    b = n[1]
    for i in range(2,len(n)):
        if int(a+b) < int(b+a):
            a += n[i]
        else:
            b += n[i]
    print(int(a)*int(b))
