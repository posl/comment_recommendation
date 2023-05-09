def purse(x):
    if x % 100 == 0:
        return "Yes"
    else:
        return "No"
x = int(input())
print(purse(x))

if __name__ == '__main__':
    purse()