def triangle(n, l):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                a = l[i]
                b = l[j]
                c = l[k]
                if a < b + c and b < c + a and c < a + b:
                    count += 1
    return count

if __name__ == '__main__':
    triangle()