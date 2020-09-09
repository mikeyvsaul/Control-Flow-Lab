# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

a = abs(int(input('Enter the lengths of the three sides of a triangle. For side "a": ')))
b = abs(int(input('For side "b": ')))
c = abs(int(input('For side "c": ')))
if a == b and b == c:
  triangle = 'equalateral'
elif a != b and b != c and a != c:
  triangle = 'scalene'
elif a == b or b == c or a == c:
  triangle = 'isosceles'
print(f'A triangle with sides of {a}, {b} & {c} is a {triangle} triangle ')
  