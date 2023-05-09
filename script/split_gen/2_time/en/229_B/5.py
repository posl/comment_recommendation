def solve(a, b):
    if len(a) > len(b):
        return "Hard"
    elif len(a) < len(b):
        return "Easy"
    else:
        for i in range(len(a)):
            if a[i] > b[i]:
                return "Hard"
            elif a[i] < b[i]:
                return "Easy"
        return "Easy"
