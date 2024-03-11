import concurrent.futures
import random as rd
import time


class Trapezoid:
    def __init__(self, trap=None):
        if trap is None:
            trap = [0, 0, 0]
        self.a = min(trap)
        self.b = max(trap)
        self.h = sum(trap) - self.a - self.b

    def __str__(self):
        return ('ტოლფერდა ტრაპეციის დიდი ფუძეა -> {}, პატარა ფუძეა -> {}, ხოლო სიმაღლეა ->{}'
                .format(self.b, self.a, self.h))

    def area(self):
        return (self.a + self.b) / 2 * self.h

    def __lt__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() < other.area()

        return False

    def __eq__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() == other.area()

        return False

    def __ge__(self, other):
        if isinstance(other, Trapezoid):
            return not self.__lt__(other)
        return False

    def __add__(self, other):
        if isinstance(other, Trapezoid):
            return self.area + other.area
        else:
            print('types did not match')

    def __sub__(self, other):
        if isinstance(other, Trapezoid):
            return abs(self.area - other.area)
        else:
            print('types did not match')

    def __mod__(self, other):
        if isinstance(other, Rectangle):
            return self.area % other.area
        else:
            raise TypeError("types did not match")


class Rectangle(Trapezoid):
    def __init__(self, re=None):
        if re is None:
            re = [0, 0]
        super().__init__([re[0], re[0], re[1]])

    def __str__(self):
        return "მართკუთხედის სიმაღლეა -> {}, ხოლო სიგანე -> {}".format(self.a, self.h)

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.area + other.area
        else:
            print('types did not match')

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            return abs(self.area - other.area)
        else:
            print('types did not match')

    def __mod__(self, other):
        if isinstance(other, Rectangle):
            return self.area % other.area
        else:
            raise TypeError("types did not match")


class Square(Rectangle):
    def __init__(self, c):
        super().__init__([c, c, c])

    def __str__(self):
        return "კვადრატის გვერდია -> {}".format(self.a)


def trapezoid_area(i):
    t = Trapezoid(i)
    print(t, "ფართობით", t.area())


def rectangle_area(i):
    r = Rectangle(i)
    print(r, "ფართობით", r.area())


def square_area(i):
    s = Square(i)
    print(s, "ფართობით", s.area())


def regular(arr):
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(trapezoid_area, arr)
        executor.map(rectangle_area, arr)
        executor.map(square_area, arr)


def threads(arr):
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(trapezoid_area, arr)
        executor.map(rectangle_area, arr)


def multiprocess(arr):
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(trapezoid_area, arr)
        executor.map(rectangle_area, arr)


if __name__ == "__main__":
    start = time.perf_counter()
    trapecoids = [[rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200)] for _ in range(100000)]
    rectangles = [[rd.randint(1, 200), rd.randint(1, 200)] for _ in range(1000)]
    squares = [rd.randint(1, 200) for _ in range(1000)]
    regular(trapecoids)
    threads(trapecoids)
    multiprocess(trapecoids)
    end = time.perf_counter()
    print(f'5 პროცესით და 20 ნაკადით პროგრამამ წაიღო {end - start} წამი')
