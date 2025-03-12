class StringCalculator:
    def _get_numbers(self, numbers):
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers[4:]  # Skip initial "//[delimiter]\n"
            return numbers.split(delimiter)
        return numbers.replace("\n", ",").split(",")

    def add(self, numbers):
        if numbers == "":
            return 0
        nums = [int(n) for n in self._get_numbers(numbers)]
        return sum(nums)
