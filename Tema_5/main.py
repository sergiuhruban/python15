class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        num = self.numerator * other.denominator + self.denominator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.numerator * other.denominator - self.denominator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def inverse(self):
        return Fraction(self.denominator, self.numerator)


def main():
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    print(f1)
    print(f2)
    f3 = f1 + f2
    print(f3)
    f3 = f1 - f2
    print(f3)

    f3 = f1.inverse()
    print(f3)


if __name__ == '__main__':
    main()
