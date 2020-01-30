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


def triangle_type():
    side_a = int(input('Enter the length of (side_a) side of a triangle: '))
    side_b = int(input('Enter the lengths of (side_b) side of a triangle: '))
    side_c = int(input('Enter the lengths of (side_c) side of a triangle: '))
    if side_a == side_b and side_c == side_a:
        print(f'A triangle with sides of {side_a}, {side_b} & {side_c} is a equalateral triangle: ')
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        print(f'A triangle with sides of {side_a}, {side_b} & {side_c} is a isosceles triangle: ')
    else:
        print(f'A triangle with sides of {side_a}, {side_b} & {side_c} is a scalene triangle: ')

triangle_type()

    

# def triangle_type int(input('eq_side_a'+'eq_side_b'+'eq_side_c') == 'equalateral':
#  print(triangle_type.format(f'A triangle with sides of {eq_side_a}, {eq_side_b}, {eq_side_c} is a (triangle_type) triangle: '))

#triangle_type('equalateral)

# a, b, c, len = "equalateral: {} {} {}", "scalene: {} {} {}", "isosceles: {} {} {}"
# if triangle_type == :  
#     print(len(triangle_type.format(f'A triangle with sides of {side_a}, {side_b} & {side_c} is a {len(triangle_type)} triangle: ')))
# elif triangle_type == 'b':
#     print(len(triangle_type.format(f'A triangle with sides of {a}, {b} & {c} is a {len(triangle_type)}  triangle: ')))
# else:
#     print(len(triangle_type.format(f'A triangle with sides of {a}, {b} & {c} is a {len(triangle_type)}  triangle: ')))