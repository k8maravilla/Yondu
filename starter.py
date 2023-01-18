'''
Project Name: Yondu Udonta
Author: Kaleb Maravilla
Due Date: 01/20/2023
Course: CS1400-002

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.

github: https://github.com/k8maravilla/Yondu/blob/master/main.py
'''

def main():
    '''
    Program starts here.
    '''
    try:
        # (1) replace pass with your code
        reavers_input = input("How many Reavers:\n")
        reavers = int(reavers_input)

        units_input = input("How many units:\n")
        units = int(units_input)
    except ValueError:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return

    # (2) replace pass with your code
    peter_quill_crew = 2

    shore_leave = (reavers-peter_quill_crew) * 3
    #print("shore leave:", shore_leave)

    remaining_units = (units - shore_leave)
    #print("remaining_units:", remaining_units)

    #step 2
    yondu_cash = remaining_units * .13
    yondus = int(yondu_cash // 1)
    #print("Yondu's share:", (yondus + yondu_crewcut))

    remaining_units = remaining_units-yondus
    #print("remaining_units:", remaining_units)

    #step 3
    peter_quill_cash = remaining_units * .11
    peter = int(peter_quill_cash // 1)

    remaining_units = remaining_units-peter
    #print("remaining_units:", remaining_units)

    #step 4
    crew_pay_cash= (remaining_units / reavers)
    #print("crew_pay_cash", crew_pay_cash)

    crew_pay_int = int(crew_pay_cash // 1)
    print("Yondu's share:", yondus + crew_pay_int)
    print("Peter's share:", peter + crew_pay_int)
    print("Crew:", crew_pay_int)

    rbf= remaining_units % reavers
    print("RBF:", rbf)

    #if crew_pay_cash == float:
        # print("leftovers:", float-crew_pay_int)

if __name__ == "__main__":
    main()
