def problem1_7():
    b1 = input("Enter the length of one of the bases: ")
    b1 = float(b1)
    b2 = input("Enter the length of the other base: ")
    b2 = float(b2)
    h = input("Enter the height: ")
    h = float(h)
    area = (1/2)*(b1+b2)*h
    print("The area of a trapezoid with bases",b1, "and",b2, "and height",h, "is",
          area)