class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        numbers = numbers.replace("\n", ",")
        # Split string of comma separated numbers and add them
        return sum(int(n) for n in numbers.split(","))
