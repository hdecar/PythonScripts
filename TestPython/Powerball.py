# Probability of winning the Powerball jackpot by matching all six numbers
regularPlaceholders = 5
powerball = 1
placeholderRange = 69
powerballRange = 26

result = 1

startNumber = placeholderRange - regularPlaceholders + 1

for i in range(startNumber, placeholderRange+1):
    result = result * i
result * powerballRange

print("Powerball odds of matching all six numbers:", result)

