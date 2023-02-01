class Vehicle {}

class Picture {
    Vehicle vehicle
}

class TwoDimensionPicture extends Picture {
    int x
    int y
}

class ThreeDimensionPicture extends Picture {
    int x
    int y
    int z
}

class Color {
    setBorderColor () {}
    fillInnerColor () {}
}

class Circle extends twoDimension implements Color {
    int originX
    int originY
    int radius

    show () {}
}


circle = Circle()
circle.setBorderColor()
circle.show()