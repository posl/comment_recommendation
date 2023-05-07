def round(x):
    if x % 1 >= 0.5:
        return int(x) + 1
    else:
        return int(x)
x = float(input())
print(round(x))
This is the first time I've ever written a program in Python, so I'm not sure if this is the best way to do it. It seems to work fine, though.
I'm not sure if there's a better way to do this, but I would probably use the round function.

if __name__ == '__main__':
    round()