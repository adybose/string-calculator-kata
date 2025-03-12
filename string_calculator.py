class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers[4:]  # Skip "//[delimiter]\n"
            return sum(int(n) for n in numbers.split(delimiter))
        numbers = numbers.replace("\n", ",")
        # Split string of comma separated numbers and add them
        return sum(int(n) for n in numbers.split(","))
