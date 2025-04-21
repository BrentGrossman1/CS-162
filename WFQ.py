

def main():
    #Input packets as a string, S=Standard, P=Priority, E=Economy
    input_packets = ["S Mary", "P Dee", "P Dee", "P Dee", "E Eileen",
                    "E Mike", "E Joe", "P Dee", "E Vicky", "E George",
                    "P Dee", "P Joe", "E Sally", "P Joe", "S Pete",
                    "P Dee", "S Bill", "S Chase", "E Price", "P Dee",
                    "E Sue"]

    # Initializing 3 queues for the 3 priority levels
    priority_queue = []
    standard_queue = []
    economy_queue = []

    # sorts the packets into individual priority queues
    for packet in input_packets:
        # iterates through the list and determines the priority by the first character
        priority = packet[0]

        if priority == "P":
            priority_queue.append(packet)
        elif priority == "S":
            standard_queue.append(packet)
        elif priority == "E":
            economy_queue.append(packet)

    # Prints the initial queues once sorted
    print("Initial Queues:")
    print("Priority Queue:", priority_queue)
    print("Standard Queue:", standard_queue)
    print("Economy Queue:", economy_queue)
    print("\nOutput after applying WFQ:")

    # Apply's the weighted fair queue algorithm
    while priority_queue or standard_queue or economy_queue:

        for _ in range(3):
            if priority_queue:
                print(priority_queue.pop(0))

        for _ in range(2):
            if standard_queue:
                print(standard_queue.pop(0))

        if economy_queue:
            print(economy_queue.pop(0))


if __name__ == "__main__":
    main()
