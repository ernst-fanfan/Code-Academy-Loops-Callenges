#Write your function here
def odd_indices(lst):
  sol = []
  for i in range(1,len(lst),2):
    sol.append(lst[i])
  return sol
#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
