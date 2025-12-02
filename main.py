# 1
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, nums))
print(result)

# 2
a = [1, 2, 3]
b = [4, 5, 6]
result = list(map(lambda x, y: x + y, a, b))
print(result)

# 3
words = ["salom", "dunyo", "python"]
result = list(map(lambda s: s.upper(), words))
print(result)

# 4
nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)

# 5
words = ["salom", "dunyo", "yaxshimisiz", "kod", "python"]
result = list(filter(lambda s: len(s) > 5, words))
print(result)
