print("==============================================")
print("          COCOMO ESTIMATION CALCULATOR")
print("==============================================")

loc = float(input("Enter Lines of Code (LOC): "))
kloc = loc / 1000

print("\nKLOC =", kloc)

modes = {
    "Organic": {
        "basic": (2.4, 1.05, 2.5, 0.38),
        "intermediate": (3.2, 1.05, 2.5, 0.38)
    },
    "Semi-Detached": {
        "basic": (3.0, 1.12, 2.5, 0.35),
        "intermediate": (3.0, 1.12, 2.5, 0.35)
    },
    "Embedded": {
        "basic": (3.6, 1.20, 2.5, 0.32),
        "intermediate": (2.8, 1.20, 2.5, 0.32)
    }
}

print("\n==============================================")
print("              BASIC COCOMO")
print("==============================================")

for mode, values in modes.items():

    a, b, c, d = values["basic"]

    effort = a * (kloc ** b)
    time = c * (effort ** d)
    staff = effort / time

    print("\nMode:", mode)
    print("Effort:", round(effort, 2), "Person-Months")
    print("Development Time:", round(time, 2), "Months")
    print("Average Staff:", round(staff, 2), "Persons")


print("\n==============================================")
print("          INTERMEDIATE COCOMO")
print("==============================================")

eaf = float(input("\nEnter Effort Adjustment Factor (EAF): "))

for mode, values in modes.items():

    a, b, c, d = values["intermediate"]

    effort = a * (kloc ** b) * eaf
    time = c * (effort ** d)
    staff = effort / time

    print("\nMode:", mode)
    print("Effort:", round(effort, 2), "Person-Months")
    print("Development Time:", round(time, 2), "Months")
    print("Average Staff:", round(staff, 2), "Persons")


print("\n==============================================")
print("              DETAILED COCOMO")
print("==============================================")

for mode, values in modes.items():

    a, b, c, d = values["intermediate"]

    effort = a * (kloc ** b) * eaf
    time = c * (effort ** d)
    staff = effort / time

    print("\nMode:", mode)
    print("Total Effort:", round(effort, 2), "Person-Months")
    print("Development Time:", round(time, 2), "Months")
    print("Average Staff:", round(staff, 2), "Persons")

    print("\nPhase-wise Effort:")
    print("Requirements Analysis:", round(effort * 0.06, 2), "Person-Months")
    print("Design:", round(effort * 0.16, 2), "Person-Months")
    print("Coding:", round(effort * 0.26, 2), "Person-Months")
    print("Testing:", round(effort * 0.34, 2), "Person-Months")
    print("Maintenance:", round(effort * 0.18, 2), "Person-Months")

print("\n==============================================")
print("             ESTIMATION COMPLETED")
print("==============================================")
