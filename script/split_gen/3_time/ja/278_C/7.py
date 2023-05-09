def follow(i, j)
  @follows[i] << j
  @follows[j] << i
end
