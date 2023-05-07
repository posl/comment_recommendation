def round(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)
print(round(float(input())))

if __name__ == '__main__':
    round()