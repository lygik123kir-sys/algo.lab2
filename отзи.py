import math

chars = {
    " ": 0.2,
    "e": 0.105,
    "t": 0.072,
    "o": 0.065,
    "a": 0.063,
    "n": 0.058,
    "i": 0.055,
    "r": 0.052,
    "s": 0.052,
    "h": 0.047,
    "d": 0.035,
    "l": 0.028,
    "c": 0.023,
    "f": 0.023,
    "u": 0.023,
    "m": 0.021,
    "p": 0.018,
    "y": 0.012,
    "w": 0.012,
    "g": 0.011,
    "b": 0.010,
    "v": 0.008,
    "k": 0.003,
    "x": 0.001,
    "j": 0.001,
    "q": 0.001,
    "z": 0.001,
}

word = "Hello baby"


bits = sum(
    chars[char.lower()] * math.log2(1 / chars[char.lower()]) for char in word
)


bytes_total = bits / 8

print(f"Слово: {word}")
print(f"В битах:  {bits:.5f} битах")
print(f"В байтах: {bytes_total:.5f} Байтах")