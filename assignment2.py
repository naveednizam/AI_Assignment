import re
# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  # +++your code here+++
  if len(s)<3:
   result = s
  elif s[-3:] == 'ing':
   result = s + 'ly'
  else:
   result = s + 'ing'
  return result


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # +++your code here+++
 match = re.search(r'not.*bad',s)
 if match:
  s= s.replace(match.group(),"good")
 return s
 
  
# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  # +++your code here+++
  #Checking Even or Odd Lengths
  #lets suppose naveedi
 if int(len(a))%2==0:
  len_e_a = int(len(a)/2)
  a_front = a[:len_e_a]
  a_back = a[len_e_a:]
 else:
  int_o_a = int(len(a)/2) + 1
  a_front = a[:int_o_a]
  a_back = a[int_o_a:]
 if int(len(b))%2==0:
  len_e_b = int(len(b)/2)
  b_front = b[:len_e_b]
  b_back = b[len_e_b:] 
 else:
  int_o_b = int(len(b)/2) + 1
  b_front = b[:int_o_b]
  b_back = b[int_o_b:]
 
 result = a_front + b_front + a_back + b_back
 return result


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  #print
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  #print
  print ('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
