def cut_wood(L, Q, queries):
    wood = [L]
    for c, x in queries:
        if c == 1:
            wood.append(x)
        else:
            wood.sort()
            idx = wood.index(x)
            print(wood[idx+1]-wood[idx])

if __name__ == '__main__':
    cut_wood()