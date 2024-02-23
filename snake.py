import tkinter as tk
import random  
import time

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.master.geometry("400x400")

        self.canvas = tk.Canvas(master, bg="black", width=400, height=400)
        self.canvas.pack()

        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.food = self.generate_food()

        self.direction = "Right"
        self.score = 0
        self.speed = 0.1

        self.draw_snake()
        self.draw_food()
        self.master.bind("<KeyPress>", self.change_direction)

        self.move_snake()

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0]+10, segment[1]+10, fill="green", tags="snake")

    def draw_food(self):
        self.canvas.delete("food")
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0]+10, self.food[1]+10, fill="red", tags="food")

    def generate_food(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        return x, y

    def change_direction(self, event):
        key = event.keysym
        if key in ["Up", "Down", "Left", "Right"]:
            self.direction = key

    def move_snake(self):
        head = self.snake[-1]
        if self.direction == "Up":
            new_head = (head[0], head[1] - 10)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + 10)
        elif self.direction == "Left":
            new_head = (head[0] - 10, head[1])
        else:
            new_head = (head[0] + 10, head[1])

        self.snake.append(new_head)
        if new_head == self.food:
            self.score += 1
            self.speed *= 0.9
            self.food = self.generate_food()
            self.draw_food()
        else:
            self.snake.pop(0)

        self.draw_snake()

        if not self.check_collision():
            self.canvas.delete("all")
            self.canvas.create_text(200, 200, text=f"Game Over\nScore: {self.score}", fill="white", font=("Arial", 20))

        else:
            self.master.after(int(self.speed * 1000), self.move_snake)

    def check_collision(self):
        head = self.snake[-1]
        if head[0] < 0 or head[0] >= 400 or head[1] < 0 or head[1] >= 400:
            return False
        if head in self.snake[:-1]:
            return False
        return True

def main():
    root = tk.Tk()
    app = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
