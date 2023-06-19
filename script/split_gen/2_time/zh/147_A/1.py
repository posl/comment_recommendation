def main():
    A = input()
    A = A.split()
    A = [int(n) for n in A]
    if sum(A) >= 22:
        print('bust')
    else:
        print('win')
