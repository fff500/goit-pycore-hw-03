import re

def normalize_phone(phone_number):
    normalized = re.sub(r"[^0-9+]", '', phone_number)
    if normalized.startswith("380"):
        normalized = "+" + normalized
    elif normalized.startswith("0"):
        normalized = "+38" + normalized
    return normalized