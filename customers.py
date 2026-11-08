# Self Assessment Questions
# Q1: I would use brackets when a field has to be there, like a customer's name, because if it's missing something is wrong and I want the error to show me. I would use .get() for fields that are optional, like email or phone, since not every customer gives those and a default keeps the program running. My rule of thumb is: if the key must exist use brackets, and if it might be missing use .get() with a default.
# Q2: Building the summary dictionary reminds me of a pivot table or SUMIF in Excel, where you add up sales for each region. The Python version is more useful for large datasets because Excel gets slow with a lot of rows and has a row limit, and I would have to rebuild the pivot table every time new data came in. The loop works the same on 3 transactions or a million, and I can just run it again on next month's data.

# --- Exercise 1 ---
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.00,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# --- Exercise 2 ---
customer["phone"] = "813-555-0142"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# --- Exercise 3 ---
email = customer.get("email", "no email on file")
print(email)

try:
    print(customer["email"])
except KeyError as error:
    print(f"KeyError caught: {error} is not in the dict anymore")

# --- Exercise 4 ---
for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives you the keys. To get the value
# you have to look it up yourself with customer[key].
for key in customer:
    print(key)

# --- Exercise 5 ---
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

discount = tier_discounts.get(customer["tier"], 0)
final_price = 200 * (1 - discount)

print(f"Tier: {customer['tier']}")
print(f"Discount: {discount:.0%}")
print(f"Final price on $200: ${final_price:.2f}")

# --- Exercise 6 ---
customers = [
    {"name": "Alice", "tier": "platinum", "ytd_spend": 1250.00},
    {"name": "Marcus", "tier": "silver", "ytd_spend": 430.00},
    {"name": "Priya", "tier": "bronze", "ytd_spend": 95.00},
]

for person in customers:
    rate = tier_discounts.get(person["tier"], 0)
    discount_amount = 300 * rate
    print(f"{person['name']} | Tier: {person['tier']} | Discount on $300: ${discount_amount:.2f}")

# --- Exercise 7 ---
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} only has {info['stock']} left")

# --- Exercise 8 ---
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

summary = {}
for sale in transactions:
    region = sale["region"]
    summary[region] = summary.get(region, 0) + sale["amount"]

for region in sorted(summary):
    print(f"{region}: {summary[region]}")
