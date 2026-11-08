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
