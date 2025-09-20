#write a program to caculete the value of sin,cos and tan using math module
import math

angle = float(input("Enter angle in degrees: "))
# Convert angle to radians
radians = math.radians(angle)

sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)

print(f"sin({angle}) = {sin_value}")
print(f"cos({angle}) = {cos_value}")
print(f"tan({angle}) = {tan_value}")
