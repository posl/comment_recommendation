def main():
    x = input()
    x = int(x)
    for a in range(-1000,1000):
        for b in range(-1000,1000):
            if a**5 - b**5 == x:
                print(a,b)
                return
