def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    A = [a%360 for a in A]
    A = [a if a <= 180 else 360-a for a in A]
    A = [a if a <= 90 else 180-a for a in A]
    A = [a if a <= 45 else 90-a for a in A]
    A = [a if a <= 22.5 else 45-a for a in A]
    A = [a if a <= 11.25 else 22.5-a for a in A]
    A = [a if a <= 5.625 else 11.25-a for a in A]
    A = [a if a <= 2.8125 else 5.625-a for a in A]
    A = [a if a <= 1.40625 else 2.8125-a for a in A]
    A = [a if a <= 0.703125 else 1.40625-a for a in A]
    A = [a if a <= 0.3515625 else 0.703125-a for a in A]
    A = [a if a <= 0.17578125 else 0.3515625-a for a in A]
    A = [a if a <= 0.087890625 else 0.17578125-a for a in A]
    A = [a if a <= 0.0439453125 else 0.087890625-a for a in A]
    A = [a if a <= 0.02197265625 else 0.0439453125-a for a in A]
    A = [a if a <= 0.010986328125 else 0.02197265625-a for a in A]
    A = [a if a <= 0.0054931640625 else 0.010986328125-a for a in A]
    A = [a if a <= 0.00274658203125 else 0.0054931640625-a for a in A]
    A = [a if a <= 0.001373291015625 else 0.00274658203125-a for a in A]
    A = [
