movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

purchases = []  

def apply_group_discount(qty, line_total):
    """10% off a line with 4+ tickets, else no change."""
    return line_total * 0.90 if qty >= 4 else line_total

def apply_member_discount(total, is_member):
    """Extra 5% off the GRAND total if member code is provided."""
    return total * 0.95 if is_member else total

print("Available movies:", ", ".join(movies.keys()))
while True:
    title = input("Enter movie title (or 'done' to finish): ").strip()
    if title.lower() == "done":
        break

    if title not in movies:
        print("Not found. Try one of:", ", ".join(movies.keys()))
        continue

    try:
        qty_str = input("Quantity: ").strip()
        qty = int(qty_str)
        if qty <= 0:
            print("Please enter a positive whole number.")
            continue
    except ValueError:
        print("Invalid quantity. Please enter a whole number.")
        continue

    purchases.append((title, qty, movies[title]))
    print(f"Added: {qty} x {title} @ ${movies[title]:.2f}")

if not purchases:
    print("\nNo purchases entered.")
    raise SystemExit


print("\n--- RECEIPT ---")
subtotal = 0.0
for title, qty, price_each in purchases:
    line = qty * price_each
    discounted_line = apply_group_discount(qty, line)
    line_note = " (10% group discount applied)" if discounted_line < line else ""
    print(f"{title:15} {qty:>3} x ${price_each:>5.2f} = ${discounted_line:>6.2f}{line_note}")
    subtotal += discounted_line


member_resp = input("\nDo you have a member code? (y/n): ").strip().lower()
is_member = member_resp.startswith("y")
total = apply_member_discount(subtotal, is_member)

print("\nSubtotal: ${:.2f}".format(subtotal))
if is_member:
    print("Member discount (5%): -${:.2f}".format(subtotal - total))
print("TOTAL:    ${:.2f}".format(total))


tickets_by_movie = {}
revenue_by_movie = {}

for title, qty, price_each in purchases:
    line = qty * price_each
    line = apply_group_discount(qty, line)

    tickets_by_movie[title] = tickets_by_movie.get(title, 0) + qty
    revenue_by_movie[title] = revenue_by_movie.get(title, 0.0) + line

print("\n--- SALES SUMMARY ---")
print(f"{'Title':15} {'Tickets':>7} {'Revenue':>10}")
for title in movies.keys(): 
    t = tickets_by_movie.get(title, 0)
    r = revenue_by_movie.get(title, 0.0)
    print(f"{title:15} {t:>7} ${r:>9.2f}")

top_title = None
top_qty = -1
for title, qty in tickets_by_movie.items():
    if qty > top_qty:
        top_title, top_qty = title, qty

sorted_by_rev = sorted(revenue_by_movie.items(), key=lambda kv: kv[1], reverse=True)

total_tickets = sum(q for _, q, _ in purchases)
avg_tix_per_purchase = total_tickets / len(purchases)

print("\n--- ANALYTICS ---")
print(f"Top seller by tickets: {top_title} ({top_qty})")
print("Titles by revenue (desc):")
for title, rev in sorted_by_rev:
    print(f"  {title:15} ${rev:,.2f}")
print(f"Average tickets per purchase: {avg_tix_per_purchase:.2f}")
