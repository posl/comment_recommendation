def main():
    n = input()
    ans = 0
    for i in range(1, len(n)):
        a = int(n[0:i])
        b = int(n[i:len(n)])
        if ans < a * b:
            ans = a * b
    print(ans)
