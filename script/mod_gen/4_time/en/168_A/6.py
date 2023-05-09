def honponbon(n):
    if n%10 in [2,4,5,7,9]:
        return "hon"
    elif n%10 in [0,1,6,8]:
        return "pon"
    else:
        return "bon"

if __name__ == '__main__':
    honponbon()