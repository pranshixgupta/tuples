def enter_group_details():
    group_name = input("Enter group name: ")
    group_size = input("Enter group size: ")
    competition_date = input("Enter competition date: ")
    venue = input("Enter venue: ")
    medal_type = input("Enter type of medal: ")
    return (group_name, group_size, competition_date, venue, medal_type)

def main():
    groups = []
    for i in range(5):
        print(f"Enter details for group {i+1}:")
        group_details = enter_group_details()
        groups.append(group_details)

    print("\nGroup Details:")
    for idx, group in enumerate(groups, start=1):
        print(f"\nGroup {idx}:")
        print("Group Name:", group[0])
        print("Group Size:", group[1])
        print("Competition Date:", group[2])
        print("Venue:", group[3])
        print("Medal Type:", group[4])

if __name__ == "__main__":
    main() 