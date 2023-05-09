def main():
    a,b = map(int, input().split())
    g = 1
    t = 0
    while True:
        if a/(g**0.5) < b:
            break
        else:
            g += 1
            t += b
    print(t + a/(g**0.5))
