with open("locations.txt") as file: location_list = file.read().split()
print(sum(abs(int(location_1) - int(location_2)) for location_1, location_2 in zip(sorted(location_list[::2]), sorted(location_list[1::2]))))
