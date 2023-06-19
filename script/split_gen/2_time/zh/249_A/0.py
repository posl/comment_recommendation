def main():
    A, B, C, D, E, F, X = map(int, input().split())
    distance_takahashi = 0
    distance_aoki = 0
    for i in range(1000):
        if i % (A + B + C) < A:
            distance_takahashi += 1
        if i % (D + E + F) < D:
            distance_aoki += 1
        if distance_takahashi == distance_aoki:
            print("draw")
            return
        if distance_takahashi > distance_aoki:
            print("Takahashi")
            return
        if distance_takahashi < distance_aoki:
            print("Aoki")
            return
