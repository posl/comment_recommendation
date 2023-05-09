def follow(i, j)
  @follows[i] << j
  @follows[j] << i
end

if __name__ == '__main__':
    follow()