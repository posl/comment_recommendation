def purse(x):
    if x % 100 == 0 and x <= 1000 and x >= 0:
        return "Yes"
    else:
        return "No"
print purse(500)
print purse(40)
print purse(0)

if __name__ == '__main__':
    purse()