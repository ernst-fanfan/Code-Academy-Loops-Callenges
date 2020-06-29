#Write your function here
def larger_sum(lst1, lst2):
  largest = lst1
  t1, t2 = sum(lst1), sum(lst2)
  if (t2 > t1):
    largest = lst2
  return largest
#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
