def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def is_even(n):
    return n % 2 == 0


def triangle_area(b, h=1):
    return 0.5 * b * h

print(fahrenheit_to_celsius(100))   
print(is_even(4))                   
print(is_even(7))                   
print(triangle_area(10))            
print(triangle_area(10, 5))
