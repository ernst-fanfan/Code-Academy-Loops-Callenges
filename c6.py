#Write your function here
def larger_sum(lst1, lst2):
  largest = lst1
  if (sum(lst2) > sum(lst1)):
    largest = lst2
  return largest
#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
