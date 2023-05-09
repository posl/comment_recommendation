def main():
    n = int(input())
    h = list(map(int, input().split()))
    #print(n, h)
    max_h = max(h)
    #print(max_h)
    count = 0
    while True:
        #print(h)
        if max_h == 0:
            break
        for i in range(n):
            if h[i] >= max_h:
                count += 1
                while True:
                    if i == n - 1:
                        break
                    if h[i+1] == 0:
                        break
                    i += 1
            else:
                while True:
                    if i == n - 1:
                        break
                    if h[i+1] == 0:
                        break
                    i += 1
        max_h -= 1
    print(count)
