# Water Jug Problem with 3 jugs using if-else only

# Taking input from user
cj1, cj2, cj3 = map(int, input("Enter capacities of jug1, jug2 and jug3: ").split())
goal = int(input("Enter the goal amount: "))
j1 = 0
j2 = 0
j3 = 0
steps = []

while True:
    if len(steps) > 50:   # limit steps to avoid infinite loop
        steps.append("No solution found.")
        break

    if j1 == goal or j2 == goal or j3 == goal:
        steps.append(f"Goal reached: ({j1}, {j2}, {j3})")
        break

    # If jug1 is empty, fill it
    if j1 == 0:
        j1 = cj1
        steps.append(f"Fill jug1: ({j1}, {j2}, {j3})")

    # Else if jug2 is not full, pour from jug1 to jug2
    elif j2 < cj2:
        pour = min(j1, cj2 - j2)
        j1 -= pour
        j2 += pour
        steps.append(f"Pour jug1 -> jug2: ({j1}, {j2}, {j3})")

    # Else if jug3 is not full, pour from jug1 to jug3
    elif j3 < cj3:
        pour = min(j1, cj3 - j3)
        j1 -= pour
        j3 += pour
        steps.append(f"Pour jug1 -> jug3: ({j1}, {j2}, {j3})")

    # Else if jug2 is full, empty it
    elif j2 == cj2:
        j2 = 0
        steps.append(f"Empty jug2: ({j1}, {j2}, {j3})")

    # Else if jug3 is full, empty it
    elif j3 == cj3:
        j3 = 0
        steps.append(f"Empty jug3: ({j1}, {j2}, {j3})")

for step in steps:
    print(step)
