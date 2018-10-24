#def KelvinToFahrenheit(Temperature):
#   assert (Temperature >= 0),"Colder than absolute zero!"
#   return ((Temperature-273)*1.8)+32

#print (KelvinToFahrenheit(273))
#print (int(KelvinToFahrenheit(505.78)))
#print (KelvinToFahrenheit(-5))


from math import gcd

a = [1, 3, 4]   #will work for an int array of any length
lcm = a[0]
for i in a[1:]:
  lcm = lcm*i//gcd(lcm, i)
print (lcm)
import math
from fractions import Fraction
from decimal import Decimal
variable = Fraction(1,3)*(Fraction(1,1)+Fraction(1,3)+Fraction(2,4))
print(Fraction(1,3)*(Fraction(1,1)+Fraction(1,3)+Fraction(2,4)))
print(math.modf(variable)[0])


print(math.modf(Fraction(1, len(max_levels)) * (Fraction(levels[0], max_levels[0]) + Fraction(levels[1], max_levels[1]) + Fraction(levels[2], max_levels[2])))[0])
    d = math.modf(Fraction(1, len(max_levels)) * (Fraction(levels[0], max_levels[0]) + Fraction(levels[1], max_levels[1]) + Fraction(levels[2], max_levels[2])))[0]
compute_distortion([1, 1, 2], [1, 3, 4])
