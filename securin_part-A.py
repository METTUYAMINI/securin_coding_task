number_of_faces = 6
number_of_dices = 2

total_combinations = (number_of_faces) ** (number_of_dices)

print(f"Total Combinations are {total_combinations}.")

distributions = []

# calculate distributiions and append result to distributions list
for dice_1 in range(1, number_of_faces + 1):
    for dice_2 in range(1, number_of_faces + 1):
        total_comb = dice_1 + dice_2
        result = {
            "Sum" : total_comb,
            "Die A" : dice_1,
            "Die B" : dice_2
        }
        distributions.append(result)
        
print(distributions)

probability = {}

for dice_1 in range(1, number_of_faces + 1):
    for dice_2 in range(1, number_of_faces + 1):
        total = dice_1 + dice_2
        probability[str(total)] = str(probability.get(total, 0) + 1) + f"/{total_combinations}"
        
print(probability)