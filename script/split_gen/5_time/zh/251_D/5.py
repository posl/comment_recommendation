def get_gcd(a,b):
    if a<b:
        a,b=b,a
    if b==0:
        return a
    return get_gcd(b,a%b)
