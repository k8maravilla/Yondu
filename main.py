#step 1
reavers_input = input("How many Reavers:\n")
reavers = int(reavers_input)

total_units_input = input("How many units:\n")
total_units = int(total_units_input)

if total_units  < 0 or reavers < 0:
    print("Enter only positive integers for reavers and units.")
    exit()

if reavers < 3:
    print("Not enough crew.")
    exit()

if total_units <= (3 * reavers):
    print("Not enough units.")
    exit()

peter_quill_crew = 2

night_crew_units = (reavers-peter_quill_crew) * 3
print("night_crew_units:", night_crew_units)

remaining_units = (total_units-night_crew_units)
print("remaining_units:", remaining_units)

#step 2
yondu_cash = remaining_units * .13
yondus = int(yondu_cash // 1)
print("Yondu's share:", yondus)

remaining_units = remaining_units-yondus
print("remaining_units:", remaining_units)

#step 3
peter_quill_cash = remaining_units * .11
peter = int(peter_quill_cash // 1)
print("Peter's share:", peter)

remaining_units = remaining_units-peter
print("remaining_units:", remaining_units)

#step 4
crew_pay_cash= (remaining_units / reavers)
print("crew_pay_cash", crew_pay_cash)

crew_pay_int = int(crew_pay_cash // 1)
print("Crew:", crew_pay_int)

rbf= remaining_units % reavers
print("RBF:", rbf)

#if crew_pay_cash == float:
    # print("leftovers:", float-crew_pay_int)