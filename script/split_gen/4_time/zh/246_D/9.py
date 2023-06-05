def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    for a in range(1, 10**5):
        if a**3 + a**2 * a + a * a**2 + a**3 >= n:
            print(a)
            return
