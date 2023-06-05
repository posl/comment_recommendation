def is753(n):
    if n%10 == 7 or n%10 == 5 or n%10 == 3:
        return True
    elif n < 10:
        return False
    else:
        return is753(n//10)

if __name__ == '__main__':
    is753()