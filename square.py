import turtle
import argparse


def draw_square(side=100, color='blue', pensize=2):
	"""Draw a square using turtle.

	Args:
		side (int): length of each side in pixels.
		color (str): pen color.
		pensize (int): pen thickness.
	"""
	screen = turtle.Screen()
	screen.title(f"Square: side={side}, color={color}")

	t = turtle.Turtle()
	t.color(color)
	t.pensize(pensize)

	for _ in range(4):
		t.forward(side)
		t.right(90)

	turtle.done()


def main():
	parser = argparse.ArgumentParser(description="Draw a square using the turtle graphics library.")
	parser.add_argument("--side", type=int, default=100, help="Length of each side in pixels")
	parser.add_argument("--color", type=str, default="blue", help="Pen color")
	parser.add_argument("--pensize", type=int, default=2, help="Pen thickness")

	args = parser.parse_args()
	draw_square(args.side, args.color, args.pensize)


if __name__ == "__main__":
	main()

