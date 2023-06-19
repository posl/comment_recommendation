def draw(h, w, k):
    if w == 1:
        return 1
    if k == 1:
        return draw(h, w-1, 1) + draw(h, w-1, 2)
    if k == w:
        return draw(h, w-1, w-1) + draw(h, w-1, w)
    return draw(h, w-1, k-1) + draw(h, w-1, k) + draw(h, w-1, k+1)

if __name__ == '__main__':
    draw()