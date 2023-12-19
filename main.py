class IteratorWithGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.generator()

    def generator(self):
        current = self.start
        while current <= self.end:
            yield current
            current += 1

# Приклад використання
my_iterator = IteratorWithGenerator(1, 5)

for value in my_iterator:
    print(value)
