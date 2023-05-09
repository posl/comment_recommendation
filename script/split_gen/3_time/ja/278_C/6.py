def follow?(a, b)
  if $follows[a][b]
    puts 'Yes'
  else
    puts 'No'
  end
end
