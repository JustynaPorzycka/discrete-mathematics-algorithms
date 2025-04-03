class Zp:
    def __init__(self, value, prime):
        self.value = value % prime
        self.prime = prime

    def __add__(self, other):
        if isinstance(other, Zp) and self.prime == other.prime:
            return Zp((self.value + other.value) % self.prime, self.prime)
        raise ValueError("Addition is not defined for given data")

    def __sub__(self, other):
        if isinstance(other, Zp) and self.prime == other.prime:
            return Zp((self.value - other.value) % self.prime, self.prime)
        elif isinstance(other, int):
            return Zp(self.value - other, self.prime)
        raise TypeError("Modulus operation is not defined for given data")

    def __mul__(self, other):
        if isinstance(other, Zp):
            if self.prime == other.prime:
                return Zp((self.value * other.value) % self.prime, self.prime)
        elif isinstance(other, int):
            return Zp((self.value * other) % self.prime, self.prime)
        raise TypeError("Multiplication is not defined for given data")

    def __mod__(self, other):
        if isinstance(other, Zp):
            if self.prime == other.prime:
                return Zp(self.value % other.value, self.prime)
        elif isinstance(other, int):
            return Zp(self.value % other, self.prime)
        raise TypeError("Modulus operation is not defined for given data")
    
    def __truediv__(self, other):
        return self*(other.inverse())

    def __eq__(self, other):
        if isinstance(other, Zp) and self.prime == other.prime:
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return str(self.value)

    def inverse(self):
        if self.value == 0:
            raise ValueError("Inverse does not exist for zero")

        def extended_euclidean(a, b):
            if b == 0:
                return a, 1, 0
            else:
                d, x, y = extended_euclidean(b, a % b)
            return d, y, x - (a // b) * y

        gcd, x, _ = extended_euclidean(self.value, self.prime)
        if gcd != 1:
            raise ValueError("Inverse does not exist for the element")
        inverse_value = x % self.prime
        return Zp(inverse_value, self.prime)


class PolynomialZp:
    def __init__(self, coefficients, prime):
        if all(coeff == Zp(0, prime) for coeff in coefficients):
            self.coefficients = [Zp(0, prime)]
        else:
            while coefficients[-1] == Zp(0, prime):
                coefficients.pop()
            self.coefficients = coefficients
        self.prime = prime
        self.degree = len(self.coefficients) - 1

    def __add__(self, other):
        if isinstance(other, PolynomialZp) and self.prime == other.prime:
            # Pad the coefficients with zeros to match the degree
            if len(self.coefficients) < len(other.coefficients):
                self.coefficients += [Zp(0, self.prime)] * (len(other.coefficients) - len(self.coefficients))
            elif len(self.coefficients) > len(other.coefficients):
                other.coefficients += [Zp(0, self.prime)] * (len(self.coefficients) - len(other.coefficients))

            # Perform coefficient-wise addition
            result = [c1 + c2 for c1, c2 in zip(self.coefficients, other.coefficients)]
            return PolynomialZp(result, self.prime)
        raise ValueError("Addition is not defined for given data")

    def __sub__(self, other):
        if isinstance(other, PolynomialZp) and self.prime == other.prime:
            # Pad the coefficients with zeros to match the degree
            if len(self.coefficients) < len(other.coefficients):
                self.coefficients += [Zp(0, self.prime)] * (len(other.coefficients) - len(self.coefficients))
            elif len(self.coefficients) > len(other.coefficients):
                other.coefficients += [Zp(0, self.prime)] * (len(self.coefficients) - len(other.coefficients))

            # Perform coefficient-wise subtraction
            result = [c1 - c2 for c1, c2 in zip(self.coefficients, other.coefficients)]
            return PolynomialZp(result, self.prime)
        raise ValueError("Subtraction is not defined for given data")

    def __mul__(self, other):
        if isinstance(other, PolynomialZp) and self.prime == other.prime:
            degree = self.degree + other.degree 
            result = [Zp(0, self.prime) for _ in range(degree + 1)]

            for i in range(len(self.coefficients)):
                for j in range(len(other.coefficients)):
                    result[i + j] += self.coefficients[i] * other.coefficients[j]

            return PolynomialZp(result, self.prime)
        raise ValueError("Multiplication is not defined for given data")

    def __mod__(self, other):
        if self.degree < other.degree:
            return self
        pow = self.degree - other.degree
        x, y = self.coefficients[-1], other.coefficients[-1]
        z = x / y
        nextReminderCoefficients = pow * [Zp(0, self.prime)] + [z * coefficient for coefficient in other.coefficients]
        nextReminder = PolynomialZp(nextReminderCoefficients, self.prime)
        return (self - nextReminder) % other

    def __eq__(self, other):
        if isinstance(other, PolynomialZp) and self.prime == other.prime:
            if all(coeff == Zp(0, self.prime) for coeff in self.coefficients) and all(coeff == Zp(0, self.prime) for coeff in other.coefficients):
                return True
            elif self.coefficients[0] == Zp(1, self.prime) and other.coefficients[0] == Zp(1, other.prime) and \
                all(coeff == Zp(0, self.prime) for coeff in self.coefficients[1:]) and all(coeff == Zp(0, other.prime) for coeff in other.coefficients[1:]):
                return True
            else:
                return self.coefficients == other.coefficients

    def __hash__(self):
        return hash(tuple(self.coefficients))

    def __str__(self):
        terms = []
        for i, coeff in enumerate(self.coefficients[::-1]):
            power = len(self.coefficients) - 1 - i
            term = f"{coeff}x^{power}"
            terms.append(term)
        return " + ".join(terms)

    def evaluate(self, x):
        result = Zp(0, self.prime)
        power = Zp(1, self.prime)

        for coeff in self.coefficients:
            result += coeff * power
            power *= Zp(x, self.prime)
        return result