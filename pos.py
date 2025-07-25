import random

validators = {
    'Alice': 50,   # stake in coins
    'Bob': 30,
    'Charlie': 20,
}

def select_validator(validators):
    names = list(validators.keys())
    weights = list(validators.values())
    return random.choices(names, weights=weights, k=1)[0]

for i in range(5):
    chosen = select_validator(validators)
    print(f"🔐 Block {i+1} validated by: {chosen}")
