class Section:
    x1: float
    y1: float
    x2: float
    y2: float

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1

        self.x2 = x2
        self.y2 = y2

    @staticmethod
    def isLineSegmentsIntersect(section1, section2):

        x1 = section1.x1
        y1 = section1.y1

        x2 = section1.x2
        y2 = section1.y2

        x3 = section2.x1
        y3 = section2.y1

        x4 = section2.x2
        y4 = section2.y2

        denominator = (y4 - y3) * (x1 - x2) - (x4 - x3) * (y1 - y2);
        if denominator == 0:
            if (x1 * y2 - x2 * y1) * (x4 - x3) - (x3 * y4 - x4 * y3) * (x2 - x1) == 0 & (x1 * y2 - x2 * y1) * (
                    y4 - y3) - (x3 * y4 - x4 * y3) * (y2 - y1) == 0:
                print("отрезки пересекаются")
            else:
                print("отрезки не пересекаются")

        else:
            numerator_a = (x4 - x2) * (y4 - y3) - (x4 - x3) * (y4 - y2)
            numerator_b = (x1 - x2) * (y4 - y2) - (x4 - x2) * (y1 - y2)
            Ua = numerator_a / denominator
            Ub = numerator_b / denominator
            if Ua >= 0 and Ua <= 1 and Ub >= 0 and Ub <= 1:
                print("Отрезки пересекаются")
            else:
                print("Отрезки не пересекаютя")

    @staticmethod
    def isParallel(section1, section2):
        x1 = section1.x1
        y1 = section1.y1

        x2 = section1.x2
        y2 = section1.y2

        x3 = section2.x1
        y3 = section2.y1

        x4 = section2.x2
        y4 = section2.y2

        if x1 - x2 == x3 - x4:
            print("Отрезки паралельны")
        elif y1 - y2 == y3 - y4:
            print("Отрезки паралельны")
        else:
            print("Отрезки не паралельны")


if __name__ == '__main__':
    section1 = Section(1, 2, 4, 4)
    section2 = Section(4, 4, 2, 3)

    print(Section.isLineSegmentsIntersect(section1, section2))

    print(Section.isParallel(section1, section2))