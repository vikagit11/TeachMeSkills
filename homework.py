#  ЗАДАЧА:

# 🦄 “Превращение единорогов в радугу”
# Вам дан список единорогов, каждый представлен в виде словаря с полем color.
# Напишите функцию unicorns_to_rainbows(unicorns: list[dict]) -> list[str], которая превращает каждого 
# единорога в строку: "🌈 Rainbow unicorn of color COLOR", где COLOR — цвет единорога.
# unicorns = [{"color": "pink"}, {"color": "blue"}, {"color": "sparkly"}]

# результат:
# [
#   "🌈 Rainbow unicorn of color pink",
#   "🌈 Rainbow unicorn of color blue",
#   "🌈 Rainbow unicorn of color sparkly"
# ]
unicorns = [{"color": "pink"}, {"color": "blue"}, {"color": "sparkly"}]
def unicorns_to_rainbows(unicorns: list[dict]) -> list[str]:
    return [f"🌈 Rainbow unicorn of color {u['color']}" for u in unicorns]
print(unicorns_to_rainbows(unicorns))