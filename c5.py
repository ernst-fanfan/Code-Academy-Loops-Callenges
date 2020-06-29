#Write your function here
def exponents(bases, powers):
  sol = []
  for base in bases:
    for power in powers:
      sol.append(base**power)
  return sol
#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
