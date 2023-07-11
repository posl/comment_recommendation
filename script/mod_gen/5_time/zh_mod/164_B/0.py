def attack(a,b,c,d):
    while True:
        c -= b
        if c <= 0:
            return "Yes"
        a -= d
        if a <= 0:
            return "No"

if __name__ == '__main__':
    attack()