class Duck {
    String name;
    String color;

    public void quack() {
        System.out.println("quack by duck");
    }
}

class GreeHeadDuck extends Duck {
    public void quack() {
        System.out.println("quack by green head duck");
    }
}

public class Example {
    public static void main(String[] args) {
        Duck duck = new Duck();
        duck.quack();

        Duck greeheadduck = new GreeHeadDuck();
        greeheadduck.quack();
    }
}