print("Ahmed")
print("Ahmed Ayman")
print("Fakhr 3")

def search_for_a_number(numbers, num=0):
    counter = 0
    indices = []
    for i in range(len(numbers)):
        if numbers[i] == num:
            counter += 1
            indices.append(i)
    return indices
