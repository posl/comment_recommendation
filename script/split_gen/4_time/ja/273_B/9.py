def roundUp(x):
    if x%10>=5:
        return x + 10 - x%10
    else:
        return x - x%10
