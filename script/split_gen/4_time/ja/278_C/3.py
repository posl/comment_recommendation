def follow(x, y)
  if @follow[x].include?(y) && @follow[y].include?(x)
    puts 'Yes'
  else
    puts 'No'
  end
end
