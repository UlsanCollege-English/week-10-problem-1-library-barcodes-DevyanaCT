"""
HW01 — Library Barcodes → Book Titles (Chaining)

Implement a tiny hash table with chaining.
Do not add type hints. Use only the standard library.
"""

def make_table(m):
    """Return a new table with m empty buckets (lists)."""
    return [[] for _ in range(m)]

def hash_basic(s):
    """Return a simple integer hash for string s.
    Hint: sum ordinals of characters.
    """
    total = 0
    for ch in s:
        total += ord(ch)
    return total

def put(t, key, value):
    """Insert or overwrite (key, value) in table t using chaining."""
    index = hash_basic(key) % len(t)
    bucket = t[index]

    # Check if key exists, and overwrite if so
    for i, (k, v) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, value)
            return

    # Otherwise append a new pair
    bucket.append((key, value))

def get(t, key):
    """Return value for key or None if not present."""
    index = hash_basic(key) % len(t)
    bucket = t[index]

    for k, v in bucket:
        if k == key:
            return v
    return None

def has_key(t, key):
    """Return True if key exists in table t; else False."""
    index = hash_basic(key) % len(t)
    bucket = t[index]

    for k, _ in bucket:
        if k == key:
            return True
    return False

def size(t):
    """Return total number of stored pairs across all buckets."""
    count = 0
    for bucket in t:
        count += len(bucket)
    return count

if __name__ == "__main__":
    # Optional manual check (not graded)
    # TODO Step 7: try a tiny run by yourself
    pass
