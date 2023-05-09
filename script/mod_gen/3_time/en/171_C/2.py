def name(n):
    if n <= 26:
        return chr(96 + n)
    else:
        return name((n - 1) // 26) + chr(96 + (n - 1) % 26 + 1)
print(name(int(input())))
Sample Input 1
2
Sample Output 1
b
Sample Input 2
27
Sample Output 2
aa
Sample Input 3
123456789
Sample Output 3
jjddja
I don't understand why the second sample input is aa instead of aaa
It's because of the way the problem is defined. The dogs numbered 1, 2, ... are respectively given the following names: a, b, ..., z, aa, ab, ..., az, ba, bb, ..., bz, ..., za, zb, ..., zz, aaa, aab, ..., aaz, aba, abb, ..., abz, ..., zzz, aaaa, ... . So the 27th dog is named aa .
I don't understand why the second sample input is aa instead of aaa
It's because of the way the problem is defined. The dogs numbered 1, 2, ... are respectively given the following names: a, b, ..., z, aa, ab, ..., az, ba, bb, ..., bz, ..., za, zb, ..., zz, aaa, aab, ..., aaz, aba, abb, ..., abz, ..., zzz, aaaa, ... . So the 27th dog is named aa .
It's because of the way the problem is defined.
The dogs numbered 1, 2, ... are respectively given the following names: a, b, ..., z, aa, ab, ..., az, ba, bb, ..., bz, ..., za, zb, ..., zz, aaa, aab, ..., aaz, aba, abb, ..., abz, ..., zzz, aaaaa, ... . So the 27th dog is named aa .
I don't understand why the second sample input is aa instead of aaa
It's because of the way the problem is defined. The dogs numbered 1, 2, ... are respectively given the following names: a, b, ..., z, aa, ab, ..., az, ba, bb, ..., bz, ..., za, zb, ..., zz, aaa, aab, ..., aaz, aba, abb, ..., ab

if __name__ == '__main__':
    name()