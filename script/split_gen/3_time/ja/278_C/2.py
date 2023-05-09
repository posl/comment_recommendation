def find_root(x)
  return x if @parent[x] == x
  @parent[x] = find_root(@parent[x])
  return @parent[x]
end
