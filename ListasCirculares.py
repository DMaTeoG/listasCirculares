import tkinter as tk
import time
import math
from tkinter import ttk

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            last = self.head.prev
            last.next = new_node
            new_node.next = self.head
            new_node.prev = last
            self.head.prev = new_node

    def traverse(self):
        nodes = []
        if self.head is not None:
            current = self.head
            nodes.append(current.data)
            current = current.next
            while current != self.head:
                nodes.append(current.data)
                current = current.next
        return nodes

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reloj de Manecillas con Estilo")
        self.root.geometry("500x750")

        self.use_roman = False

        self.hours = CircularDoublyLinkedList()
        for i in range(12):
            self.hours.insert_at_end(i)

        self.minutes = CircularDoublyLinkedList()
        self.seconds = CircularDoublyLinkedList()
        for i in range(60):
            self.minutes.insert_at_end(i)
            self.seconds.insert_at_end(i)

        self.emoji_ranges = [
            (0, 5, "🌙"),
            (6, 11, "🌅"),
            (12, 17, "☀️"),
            (18, 23, "🌇")
        ]

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)

        self.toggle_button = ttk.Button(root, text="Cambiar a Números Romanos", command=self.toggle_style)
        self.toggle_button.pack()

        self.digital_time = ttk.Label(root, font=("Helvetica", 16))
        self.digital_time.pack()

        self.emoji_label = ttk.Label(root, font=("Helvetica", 32))
        self.emoji_label.pack(pady=5)

        self.sun_canvas = tk.Canvas(root, width=400, height=100, bg="lightblue", highlightthickness=1, highlightbackground="gray")
        self.sun_canvas.pack(pady=10)

        self.sun_message = ttk.Label(root, font=("Helvetica", 14))
        self.sun_message.pack(pady=5)

        list_info = ttk.LabelFrame(root, text="Listas Circulares Dobles", padding=10)
        list_info.pack(pady=10, padx=20, fill=tk.X)

        ttk.Label(list_info, text="Horas (0-11): " + str(self.hours.traverse())).pack(anchor=tk.W)
        ttk.Label(list_info, text="Minutos (0-59): " + str(self.minutes.traverse()[:10]) + "...").pack(anchor=tk.W)
        ttk.Label(list_info, text="Segundos (0-59): " + str(self.seconds.traverse()[:10]) + "...").pack(anchor=tk.W)

        self.update_clock()

    def toggle_style(self):
        self.use_roman = not self.use_roman
        new_text = "Cambiar a Números Romanos" if not self.use_roman else "Cambiar a Números Arábigos"
        self.toggle_button.config(text=new_text)

    def get_time_emoji(self, hour):
        for start, end, emoji in self.emoji_ranges:
            if start <= hour <= end:
                return emoji
        return "🕒"

    def get_sun_message(self, hour):
        if 6 <= hour < 9:
            return "Está amaneciendo"
        elif 9 <= hour < 11:
            return "La mañana está avanzada"
        elif 11 <= hour < 13:
            return "Es mediodía"
        elif 13 <= hour < 17:
            return "La tarde está en curso"
        elif 17 <= hour <= 18:
            return "Ya va anochecer"
        else:
            return "Es de noche"

    def draw_clock_face(self):
        self.canvas.delete("all")
        width = 400
        height = 400
        center_x = width // 2
        center_y = height // 2
        radius = 150

        self.canvas.create_oval(center_x - radius, center_y - radius, 
                                center_x + radius, center_y + radius, 
                                width=2)

        roman_numerals = ["XII", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"]

        for i in range(12):
            angle = math.radians(i * 30 - 90)
            x_text = center_x + (radius - 40) * math.cos(angle)
            y_text = center_y + (radius - 40) * math.sin(angle)
            label = roman_numerals[i] if self.use_roman else str(i if i != 0 else 12)
            self.canvas.create_text(x_text, y_text, text=label, font=("Helvetica", 12))

        for i in range(60):
            angle = math.radians(i * 6 - 90)
            x1 = center_x + (radius - (10 if i % 5 == 0 else 20)) * math.cos(angle)
            y1 = center_y + (radius - (10 if i % 5 == 0 else 20)) * math.sin(angle)
            x2 = center_x + radius * math.cos(angle)
            y2 = center_y + radius * math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, width=2 if i % 5 == 0 else 1)

    def draw_clock_hands(self, hour, minute, second):
        width = 400
        height = 400
        center_x = width // 2
        center_y = height // 2

        hour = hour % 12
        hour_angle = math.radians((hour * 30) + (minute * 0.5) - 90)
        minute_angle = math.radians((minute * 6) - 90)
        second_angle = math.radians((second * 6) - 90)

        hour_length = 70
        minute_length = 100
        second_length = 120

        hour_x = center_x + hour_length * math.cos(hour_angle)
        hour_y = center_y + hour_length * math.sin(hour_angle)
        self.canvas.create_line(center_x, center_y, hour_x, hour_y, width=4, fill="blue")

        minute_x = center_x + minute_length * math.cos(minute_angle)
        minute_y = center_y + minute_length * math.sin(minute_angle)
        self.canvas.create_line(center_x, center_y, minute_x, minute_y, width=3, fill="green")

        second_x = center_x + second_length * math.cos(second_angle)
        second_y = center_y + second_length * math.sin(second_angle)
        self.canvas.create_line(center_x, center_y, second_x, second_y, width=2, fill="red")

        self.canvas.create_oval(center_x - 5, center_y - 5, 
                                center_x + 5, center_y + 5, 
                                fill="black")

    def draw_sun_parabola(self, hour):
        self.sun_canvas.delete("all")
        width = 400
        height = 100
        points = []

        for x in range(0, width + 1, 4):
            t = x / width
            y = -4 * (t - 0.5) ** 2 + 1
            y_scaled = (1 - y) * (height - 20) + 10
            points.append((x, y_scaled))

        for i in range(len(points) - 1):
            self.sun_canvas.create_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1], fill="orange", width=2)

        if 6 <= hour <= 18:
            t = (hour - 6) / 12
            x = int(t * width)
            y = -4 * (t - 0.5) ** 2 + 1
            y_scaled = (1 - y) * (height - 20) + 10
            self.sun_canvas.create_oval(x - 8, y_scaled - 8, x + 8, y_scaled + 8, fill="yellow", outline="gold")

    def update_clock(self):
        now = time.localtime()
        hour = now.tm_hour
        minute = now.tm_min
        second = now.tm_sec

        current_emoji = self.get_time_emoji(hour)
        self.emoji_label.config(text=current_emoji)

        self.sun_message.config(text=self.get_sun_message(hour))

        self.digital_time.config(text=f"{hour:02d}:{minute:02d}:{second:02d}")

        self.draw_clock_face()
        self.draw_clock_hands(hour, minute, second)
        self.draw_sun_parabola(hour)

        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()
