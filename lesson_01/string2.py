import math

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

def verbing(s):
  if len(s) < 3:
    return s
  else:
    if s[-3:] == 'ing':
      s = s + 'ly'
    else:
      s = s + 'ing'
  return s


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

def not_bad(s):
  if "not" in s:
    not_pos = s.find("not")
    if "bad" in s:
      bad_pos = s.find("bad")
      if not_pos < bad_pos:
        s = s[:not_pos] + 'good' + s[bad_pos+3:]
      else:
        return s
    else:
      return s
  return s


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

def front_back(a, b):
  length_a = len(a)
  length_b = len(b)
  if len(a) % 2 == 0:
    even_half_of_a = math.floor(length_a / 2)
    a_front = a[0:even_half_of_a]
    a_back = a[even_half_of_a:]
  else:
    odd_half_of_a = math.floor(length_a / 2) + 1
    a_front = a[0:odd_half_of_a]
    a_back = a[odd_half_of_a:]
  if len(b) % 2 == 0:
    even_half_of_b = math.floor(length_b / 2)
    b_front = b[0:even_half_of_b]
    b_back = b[even_half_of_b:]
  else:
    odd_half_of_b = math.floor(length_b / 2) + 1
    b_front = b[0:odd_half_of_b]
    b_back = b[odd_half_of_b:]
  return a_front + b_front + a_back + b_back


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print (f'{prefix} got: {got} expected: {expected}')


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.

def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print ('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

# Call main function (run the program)
main()
