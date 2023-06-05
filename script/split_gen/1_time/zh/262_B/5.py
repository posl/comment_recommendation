def check(a, b, c, edges):
    if (a, b) in edges and (b, c) in edges and (c, a) in edges:
        return True
    else:
        return False
