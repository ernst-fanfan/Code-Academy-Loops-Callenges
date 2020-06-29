def over_nine_thousand(lst):
  sol = 0
  if (len(lst) != 0):
    if(sum(lst) < 9000):
      sol = sum(lst)
    else:
      for num in lst:
        if (sol < 9000):
          sol += num
        else:
          break
  return sol
#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
