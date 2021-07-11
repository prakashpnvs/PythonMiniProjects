def generate_steps(disks, source, destination, aux):
    """
    Function to generate the steps to transfer the disks from source tower to destination tower
    :param disks: Integer (Number of disks)
    :param source: String (Name of the source tower)
    :param destination: String (Name of the destination tower)
    :param aux: String (Name of the auxiliary tower)
    """
    if disks < 1:
        print("Enter a valid number of disks")
    elif disks == 1:
        print("Move disk from " + source + " to " + destination)
    else:
        generate_steps(disks-1, source, aux, destination)
        print("Move disk from " + source + " to " + destination)
        generate_steps(disks-1, aux, destination, source)


if __name__ == '__main__':
    generate_steps(3, "A", "B", "C")

    """
    Output as follows:
    
    Move disk from A to B
    Move disk from A to C
    Move disk from B to C
    Move disk from A to B
    Move disk from C to A
    Move disk from C to B
    Move disk from A to B
    
    """