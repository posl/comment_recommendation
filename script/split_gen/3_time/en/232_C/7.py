def solve(N,M,AB,CD):
    AB.sort()
    CD.sort()
    if AB == CD:
        return "Yes"
    else:
        return "No"
