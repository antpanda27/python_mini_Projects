def battle(my_army, opposing_army):
    # Assigning characters to strength levels in indexes
    strength = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Assigning values
    my_army_wins = 0
    opposing_army_wins = 0

    # Split characters for each argument into a list
    my_army_list = []
    for x in my_army:
        my_army_list.append(x)

    opposing_army_list = []
    for x in opposing_army:
        opposing_army_list.append(x)

    # Convert characters into numbers
    def convert(army_list):
        for i in range(len(army_list)):
            if army_list[i].isalpha():
                army_list[i] = strength.index(army_list[i])
            elif army_list[i].isdigit():
                army_list[i] = int(army_list[i])
            else:
                army_list[i] = 0

    convert(my_army_list)
    convert(opposing_army_list)

    # Results for when there are more characters on one side (retreating), then find the results of the battles
    if len(my_army) > len(opposing_army):
        return "Opponent retreated"
    elif len(my_army) < len(opposing_army):
        return "We retreated"
    else:

        # Compare values between both arguments
        for i in range(len(my_army_list)):
            if my_army_list[i] > opposing_army_list[i]:
                my_army_wins += 1
            elif my_army_list[i] < opposing_army_list[i]:
                opposing_army_wins += 1
            else:
                continue

        if my_army_wins > opposing_army_wins:
            return "We won"
        elif my_army_wins < opposing_army_wins:
            return "We lost"
        elif my_army_wins == opposing_army_wins:
            return "It was a tie"
    print(my_army_list)
    print(opposing_army_list)


battle("Mr. Smith", "Dr. Jones")