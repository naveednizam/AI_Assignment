# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
 if len(nums)>0:
  list_nums=list(set(nums))
 else:
   list_nums=nums
 # +++your code here+++
 result = list_nums
 return result


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  # +++your code here+++
 #list = list1 + list2
 #list.sort()
 
 result = []
 ## loop through len of list 1 and list 2
 while len(list1) and len(list2):
  ##Below linear expression states that if last element of list 1 is greater than last element of list 2 then list1 else list 2 
  ##and pop the last element of the list and append it into result So on first loop zz is greater than cc thats why it takes list1 and pop its last element zz,
  ##and append it into result set now list have two elements aa,xx again loop through and print append xx again loop through and append cc again loop through
  ##then len of list 2 is 0 it comes out of loop then check len of list 1 and 2 if exists than append elements in the result set. then slicing the list to get the require list.
  result.append((list1 if list1[-1] > list2[-1] else list2).pop(-1))
 result += list1 if len(list1) else list2
 return result[-1::-1]
 

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print ('remove_adjacent')
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  #print
  print ('linear_merge')
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
