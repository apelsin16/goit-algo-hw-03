import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order-1, size/3)
            t.left(angle)

def snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def main():
    # Запит на рівень рекурсії від користувача
    order = int(input("Введіть рівень рекурсії (ціле число більше 0): "))
    
    if order <= 0:
        print("Рівень рекурсії повинен бути цілим числом більше 0.")
        return
    
    # Створення вікна для малювання
    wn = turtle.Screen()
    wn.bgcolor("white")

    # Створення черепахи
    alex = turtle.Turtle()
    alex.color("blue")
    alex.speed(0)  # Найшвидше малювання

    # Малювання сніжинки Коха з вказаним рівнем рекурсії
    snowflake(alex, order, 300)

    # Завершення роботи
    wn.mainloop()

if __name__ == "__main__":
    main()