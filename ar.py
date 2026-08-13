
# Simple art billing CLI demonstrating use of functions and callbacks


CATALOG = {
	1: {"name": "Acrylic Landscape", "price": 120.0},
	2: {"name": "Watercolor Portrait", "price": 85.0},
	3: {"name": "Ink Sketch", "price": 40.0},
	4: {"name": "Digital Print", "price": 25.0},
}


def list_items() -> None:
	print("Available art pieces:")
	for item_id, info in CATALOG.items():
		print(f"{item_id}: {info['name']} — ${info['price']:.2f}")


def add_to_cart(cart: Dict[int, int], item_id: int, qty: int = 1) -> None:
	if item_id not in CATALOG:
		raise ValueError("Item not found in catalog")
	cart[item_id] = cart.get(item_id, 0) + qty


def calculate_subtotal(cart: Dict[int, int]) -> float:
	return sum(CATALOG[i]["price"] * q for i, q in cart.items())


def apply_tax(amount: float, tax_rate: float = 0.05) -> float:
	return amount * (1 + tax_rate)


def calculate_total(
	cart: Dict[int, int],
	tax_fn: Callable[[float], float] = lambda x: apply_tax(x, 0.05),
	discount_fn: Optional[Callable[[float], float]] = None,
) -> Tuple[float, float, float]:
	"""Return (subtotal, discount_amount, total_with_tax)

	- `tax_fn` is a function that takes an amount and returns amount after tax.
	- `discount_fn` is an optional function that takes subtotal and returns discount amount.
	"""
	subtotal = calculate_subtotal(cart)
	discount = discount_fn(subtotal) if discount_fn else 0.0
	taxed = tax_fn(max(0.0, subtotal - discount))
	return subtotal, discount, taxed


def format_invoice(
	cart: Dict[int, int], subtotal: float, discount: float, total: float, customer: str = "Customer"
) -> str:
	lines = []
	lines.append("INVOICE")
	lines.append(f"Date: {datetime.now().isoformat(' ', 'seconds')}")
	lines.append(f"Customer: {customer}")
	lines.append("\nItems:")
	for item_id, qty in cart.items():
		info = CATALOG[item_id]
		lines.append(f" - {info['name']} x{qty} @ ${info['price']:.2f} = ${info['price']*qty:.2f}")
	lines.append(f"\nSubtotal: ${subtotal:.2f}")
	lines.append(f"Discount: -${discount:.2f}")
	lines.append(f"Total (incl. tax): ${total:.2f}")
	return "\n".join(lines)


def save_invoice(text: str, filename: str) -> None:
	with open(filename, "w", encoding="utf-8") as f:
		f.write(text)


def sample_member_discount(subtotal: float) -> float:
	"""Example discount callback: 10% off for members over $50"""
	return subtotal * 0.10 if subtotal > 50 else 0.0


def run_cli() -> None:
	cart: Dict[int, int] = {}
	print("Welcome to the Art Billing Tool")
	while True:
		print("\nCommands: list, add, view, checkout, savecart, loadcart, quit")
		cmd = input("> ").strip().lower()
		if cmd == "list":
			list_items()
		elif cmd.startswith("add"):
			# usage: add 2 3  (item_id qty)
			parts = cmd.split()
			try:
				if len(parts) < 2:
					print("Usage: add <item_id> [qty]")
					continue
				item_id = int(parts[1])
				qty = int(parts[2]) if len(parts) > 2 else 1
				add_to_cart(cart, item_id, qty)
				print("Added to cart.")
			except Exception as e:
				print("Error:", e)
		elif cmd == "view":
			if not cart:
				print("Cart is empty")
			else:
				for i, q in cart.items():
					print(f"{CATALOG[i]['name']} x{q} — ${CATALOG[i]['price']*q:.2f}")
				print(f"Subtotal: ${calculate_subtotal(cart):.2f}")
		elif cmd == "savecart":
			fname = input("Filename to save cart (json): ").strip() or "cart.json"
			with open(fname, "w", encoding="utf-8") as f:
				json.dump(cart, f)
			print(f"Cart saved to {fname}")
		elif cmd == "loadcart":
			fname = input("Filename to load cart from (json): ").strip() or "cart.json"
			try:
				with open(fname, "r", encoding="utf-8") as f:
					data = json.load(f)
				cart = {int(k): int(v) for k, v in data.items()}
				print("Cart loaded.")
			except Exception as e:
				print("Failed to load cart:", e)
		elif cmd == "checkout":
			if not cart:
				print("Cart is empty")
				continue
			customer = input("Customer name: ").strip() or "Customer"
			# choose discount type to demonstrate passing functions
			print("Discounts: none, member")
			d = input("Discount type: ").strip().lower()
			discount_fn = sample_member_discount if d == "member" else None
			subtotal, discount, total = calculate_total(cart, tax_fn=lambda x: apply_tax(x, 0.05), discount_fn=discount_fn)
			invoice = format_invoice(cart, subtotal, discount, total, customer)
			print("\n" + invoice)
			if input("Save invoice to file? (y/N): ").strip().lower() == "y":
				fname = f"invoice_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
				save_invoice(invoice, fname)
				print(f"Saved invoice to {fname}")
			# clear cart after checkout
			cart.clear()
		elif cmd == "quit":
			print("Goodbye")
			break
		else:
			print("Unknown command")


if __name__ == "__main__":
	run_cli()

