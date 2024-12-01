with open("locations.txt") as file: location_list = file.read().split()
print(sum(int(i) * location_list[1::2].count(i) for i in location_list[::2]))
