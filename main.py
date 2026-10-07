# main.py

# add sample inputs
from business_rules import (
    apply_discount,
    calculate_total,
    get_approval_tier,
    requires_review,
)

price, qty = 450.00, 3

total = calculate_total(price, qty)
review = requires_review(total)
tier = get_approval_tier(total)
discounted_price = apply_discount(price, 10)

print(f"Total: {total:.2f}")
print(f"Requires Review: {review}")
print(f"Approval Tier: {tier}")
print(f"10% discount: {discounted_price:.2f}")
