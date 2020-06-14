newEngland = ["Maine","New Hampshire","Vermont", "Rhode Island", 
"Massachusetts","Connecticut"]

def problem2_3(ne):
    for state in ne:
        lettercount = len(state)
        print(state, "has", lettercount, "letters.")