#Validation is done by trusted validators

validators = ['Alice', 'Bob', 'Charlie']

def select_authority(validators, round_number):
    return validators[round_number % len(validators)]

for i in range(5):
    validator = select_authority(validators, i)
    print(f"🏛 Block {i+1} validated by authority: {validator}")
