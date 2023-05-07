def get_good_integers(n, w, a):
    good_integers = set()
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                good_integers.add(a[i])
                good_integers.add(a[j])
                good_integers.add(a[k])
                good_integers.add(a[i] + a[j])
                good_integers.add(a[i] + a[k])
                good_integers.add(a[j] + a[k])
                good_integers.add(a[i] + a[j] + a[k])
    good_integers = [x for x in good_integers if x <= w]
    return len(good_integers)

if __name__ == '__main__':
    get_good_integers()