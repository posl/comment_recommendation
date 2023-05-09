def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    sum_h = h1 + h2 + h3
    sum_w = w1 + w2 + w3
    if sum_h != sum_w:
        print(0)
        return
    else:
        sum_h = sum_h // 3
        sum_w = sum_w // 3
    if h1 != w1:
        print(0)
        return
    if h1 + h2 != w1 + w2:
        print(0)
        return
    if h1 + h2 + h3 != w1 + w2 + w3:
        print(0)
        return
    if h1 + h3 != w1 + w3:
        print(0)
        return
    if h1 + h2 + h3 != sum_h * 3:
        print(0)
        return
    if h1 + h2 != sum_h * 2:
        print(0)
        return
    if h1 != sum_h:
        print(0)
        return
    if h1 + h3 != sum_h * 2:
        print(0)
        return
    if h1 + h2 + h3 != sum_w * 3:
        print(0)
        return
    if h1 + h2 != sum_w * 2:
        print(0)
        return
    if h1 != sum_w:
        print(0)
        return
    if h1 + h3 != sum_w * 2:
        print(0)
        return
    if h1 + h2 + h3 != sum_w * 3:
        print(0)
        return
    if h1 + h2 != sum_w * 2:
        print(0)
        return
    if h1 != sum_w:
        print(0)
        return
    if h1 + h3 != sum_w * 2:
        print(0)
        return
    if h1 == w1:
        if h1 + h2 == w1 + w2:
            if h1 + h2 + h3 == w1 + w2 + w3:
                if h1 + h3 == w1 + w3:
                    print(1)
                    return

if __name__ == '__main__':
    main()