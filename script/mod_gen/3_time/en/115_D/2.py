def burger(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    else:
        a = 2 ** (n + 1) - 3
        b = 2 ** n - 1
        if x == 1:
            return 0
        elif x <= 1 + a:
            return burger(n - 1, x - 1)
        elif x == 2 + a:
            return b
        elif x <= 2 + 2 * a:
            return b + burger(n - 1, x - 2 - a)
        else:
            return 2 * b
n, x = map(int, input().split())
print(burger(n, x))
I'm not sure what the problem is, but I think it's the burger function. It's a recursive function, and I think that's where the problem is.
I'm not sure how to debug this. I'm not sure what the problem is, but I think it's the burger function. It's a recursive function, and I think that's where the problem is.I'm not sure how to debug this.
I'm not sure what the problem is, but I think it's the burger function. It's a recursive function, and I think that's where the problem is.I'm not sure how to debug this.
I'm not sure what the problem is, but I think it's the burger function. It's a recursive function, and I think that's where the problem is.I'm not sure how to debug this.
I'm not sure what the problem is, but I think it's the burger function. It's a recursive function, and I think that's where the problem is.I'm not sure how to debug this.
I'm not sure what the problem is, but I think it's the burger function. It's a recursive function, and I think that's where the problem is.I'm not sure how to debug this.
I'm not sure what the problem is, but I think it's the burger function. It's a recursive function, and I think that's where the problem is.I'm not sure how to debug this.
I'm not sure what the problem is, but I think it's the burger function. It's a recursive function, and I think that's where the problem is.I'm not sure how to debug this.
I'm not sure

if __name__ == '__main__':
    burger()