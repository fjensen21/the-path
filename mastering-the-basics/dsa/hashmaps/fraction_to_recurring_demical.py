def fraction_to_decimal(numerator, denominator):
    result = ""
    quotient = 0
    remainder = 0
    remainder_map = {}

    if numerator == 0:
        return "0"

    if numerator < 0 or denominator < 0:
        result += "-"
        numerator = abs(numerator)
        denominator = abs(denominator)

    quotient = numerator / denominator
    remainder = (numerator % denominator) * 10

    result += str(int(quotient))

    if remainder == 0:
        return result

    result += "."

    while remainder != 0:
        if remainder in remainder_map:
            beginning_of_recurring = remainder_map[remainder]
            before_recurring = result[0:beginning_of_recurring]
            recurring = result[beginning_of_recurring : len(result)]
            result = before_recurring + "(" + recurring + ")"
            return result

        remainder_map[remainder] = len(result)
        quotient = remainder / denominator
        result += str(int(quotient))
        remainder = (remainder % denominator) * 10

    return result


if __name__ == "__main__":
    expected = "2.6(1)"
    actual = fraction_to_decimal(47, 18)
    print(f"Expected: {expected}\nActual:{actual}")
