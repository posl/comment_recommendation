def main():
  a, b, h, m = map(int, input().split())
  h_angle = (h * 60 + m) / 2
  m_angle = m * 6
  angle = min(abs(h_angle - m_angle), 360 - abs(h_angle - m_angle))
  print((a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(angle))) ** 0.5)

if __name__ == '__main__':
    main()