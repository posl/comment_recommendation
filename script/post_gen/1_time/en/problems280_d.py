Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K = int(input())
    N = K
    i = 2
    while i * i <= K:
        if K % i == 0:
            while K % i == 0:
                K = K // i
            N = N // i * (i - 1)
        i += 1
    if K > 1:
        N = N // K * (K - 1)
    print(N)

=======
Suggestion 2

def prime_factorization(n):
    pf = {}
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            pf[i] = pf.get(i, 0) + 1
            n //= i
    if n != 1:
        pf[n] = pf.get(n, 0) + 1
    return pf

k = int(input())
pf = prime_factorization(k)
ans = 1
for p in pf:
    ans *= p ** (pf[p] // len(str(p)))
print(ans)

=======
Suggestion 3

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 4

def main():
    K = int(input())
    prime = []
    i = 2
    while i*i <= K:
        if K % i == 0:
            prime.append(i)
            while K % i == 0:
                K //= i
        i += 1
    if K > 1:
        prime.append(K)
    ans = 1
    for p in prime:
        i = p
        while i <= K:
            i *= p
        ans *= i//p
    print(ans)

main()

=======
Suggestion 5

def main():
    k = int(input())
    n = 1
    while True:
        if k%n == 0:
            k = k//n
            n = 1
        if k == 1:
            break
        n += 1
    print(n)

main()

=======
Suggestion 6

def get_prime_factorization(n):
    prime_factorization = []
    for i in range(2, int(n**0.5)+1):
        if n == 1:
            break
        while n%i == 0:
            prime_factorization.append(i)
            n //= i
    if n != 1:
        prime_factorization.append(n)
    return prime_factorization

=======
Suggestion 7

def prime_factorization(n):
    #n=2*3*5*7*11*13*17*19*23*29*31*37*41*43*47*53*59*61*67*71*73*79*83*89*97*101*103*107*109*113*127*131*137*139*149*151*157*163*167*173*179*181*191*193*197*199*211*223*227*229*233*239*241*251*257*263*269*271*277*281*283*293*307*311*313*317*331*337*347*349*353*359*367*373*379*383*389*397*401*409*419*421*431*433*439*443*449*457*461*463*467*479*487*491*499*503*509*521*523*541*547*557*563*569*571*577*587*593*599*601*607*613*617*619*631*641*643*647*653*659*661*673*677*683*691*701*709*719*727*733*739*743*751*757*761*769*773*787*797*809*811*821*823*827*829*839*853*857*859*863*877*881*883*887*907*911*919*929*937*941*947*953*967*971*977*983*991*997*1009*1013*1019*1021*1031*1033*1039*1049*1051*1061*1063*1069*1087*1091*1093*1097*1103*1109*1117*1123*1129*1151*1153*1163*1171*1181*1187*1193*1201*1213*1217*1223*1229*1231*1237*1249*1259*1277*1279*1283*1289*1291*1297*1301*1303*1307*1319*1321*1327*1361*1367*1373

=======
Suggestion 8

def main():
    k = int(input())
    n = k
    for i in range(2, 100000):
        if n % i == 0:
            n = n // i
            i = 1
        if n == 1:
            print(i)
            exit()

=======
Suggestion 9

def main():
    import math
    k = int(input())
    if k%2 == 0:
        print(2)
        exit()
    if k%5 == 0:
        print(5)
        exit()
    for i in range(3, math.ceil(math.sqrt(k))+1, 2):
        if k%i == 0:
            print(i)
            exit()
    print(k)

main()

=======
Suggestion 10

def main():
    K = int(input())
    #print(K)
    #print(type(K))
    #print(K%2)
    #print(K%5)
    #print(K%10)
    #print(K%11)
    #print(K%12)
    #print(K%13)
    #print(K%14)
    #print(K%15)
    #print(K%16)
    #print(K%17)
    #print(K%18)
    #print(K%19)
    #print(K%20)
    #print(K%21)
    #print(K%22)
    #print(K%23)
    #print(K%24)
    #print(K%25)
    #print(K%26)
    #print(K%27)
    #print(K%28)
    #print(K%29)
    #print(K%30)
    #print(K%31)
    #print(K%32)
    #print(K%33)
    #print(K%34)
    #print(K%35)
    #print(K%36)
    #print(K%37)
    #print(K%38)
    #print(K%39)
    #print(K%40)
    #print(K%41)
    #print(K%42)
    #print(K%43)
    #print(K%44)
    #print(K%45)
    #print(K%46)
    #print(K%47)
    #print(K%48)
    #print(K%49)
    #print(K%50)
    #print(K%51)
    #print(K%52)
    #print(K%53)
    #print(K%54)
    #print(K%55)
    #print(K%56)
    #print(K%57)
    #print(K%58)
    #print(K%59)
    #print(K%60)
    #print(K%61)
    #print(K%62)
    #print(K%63)
    #print(K%64)
    #print(K%65)
    #print(K%66)
    #print(K%67)
    #print(K%68)
    #print(K%69)
    #print(K%70)
    #print(K%71)
    #print(K%72)
    #print(K%73)
    #print(K%74)
    #print(K%75)
    #print(K%
