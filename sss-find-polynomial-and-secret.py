from sympy import symbols, simplify, Poly

def find_function(points, prime):
    x, y = symbols('x y')
    polynomial = 0

    for i in range(len(points)):
        term = points[i][1]
        for j in range(len(points)):
            if i != j:
                term *= (x - points[j][0]) / (points[i][0] - points[j][0])
        polynomial += term

    poly = Poly(polynomial, x)
    coefficients = poly.all_coeffs()
    coefficients = [coeff for coeff in coefficients]
    numerators = [coeff.numerator for coeff in coefficients]
    denominators = [coeff.denominator for coeff in coefficients]
    coefficients_mod_prime = [((n*pow(d,-1,prime))%prime)  for (n,d) in zip(numerators,denominators)]

    function = ""
    for i, coeff in enumerate(coefficients_mod_prime):
        if coeff != 0:
            function += f" + {coeff}x^{-1-i+len(coefficients_mod_prime)}"

    for i in range(len(points)):
        print(f"Point {i+1} = {points[i]}")

    print("\nPrime =", prime)
    print("\nf(x) =", function)
    print("\nSecret =", coefficients_mod_prime[-1])

points = [
    (1, 5028699408156100069577949335717369259),
    (2, 1289827703178428571335141546319942185),
    (3, 158924568345536217236958880347691825739),
    (4, 137650554414291002603074558308064808467),
    (5, 107608969369912016401369479143322996096),
    (6, 68799813212399258631843642853466388626),
    (7, 21223085941752729294497049438494986057),
    (8, 135019971018441660121017002614292894116),
    (9, 69908101521527587648028894949091901349),
    (10, 166169844371948975338907333874660219210)
]

prime = 2 ** 127 - 1

find_function(points, prime)

"""

OUTPUT

Point 1 = (1, 5028699408156100069577949335717369259)
Point 2 = (2, 1289827703178428571335141546319942185)
Point 3 = (3, 158924568345536217236958880347691825739)
Point 4 = (4, 137650554414291002603074558308064808467)
Point 5 = (5, 107608969369912016401369479143322996096)
Point 6 = (6, 68799813212399258631843642853466388626)
Point 7 = (7, 21223085941752729294497049438494986057)
Point 8 = (8, 135019971018441660121017002614292894116)
Point 9 = (9, 69908101521527587648028894949091901349)
Point 10 = (10, 166169844371948975338907333874660219210)

Prime = 170141183460469231731687303715884105727

f(x) =  + 80686806173667730081933273295384655314x^2 + 94483076694957601719331979756216818438x^1 + 1234x^0

Secret = 1234

"""
