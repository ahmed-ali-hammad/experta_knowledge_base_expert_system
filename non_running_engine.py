from base import *

"""
This Knowledge Engine covers the case when the engine doesn't start
"""

class NonRunningCarDiagnosis(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        """
        will be called every time the reset method is called.
        """
        yield Fact(action="find_fault")

    """
    USER INPUT
    """

    @Rule(Fact(action='find_fault'), NOT(Fact(headlights_light=W())))
    def sign_1(self):
        self.declare(Fact(headlights_light=input_yes_no("Headlights light up when you switch them on: ").strip().lower()))

    @Rule(Fact(action='find_fault'), NOT(Fact(cranks_slowly=W())))
    def sign_3(self):
        self.declare(Fact(cranks_slowly=input_yes_no("Engine cranks slowly when you turn a key: ").strip().lower()))

    @Rule(Fact(action='find_fault'), NOT(Fact(headlights_dim=W())))
    def sign_4(self):
        self.declare(Fact(headlights_dim=input_yes_no("Headlights dim when you to try the starter: ").strip().lower()))

    @Rule(Fact(action='find_fault'), NOT(Fact(gas_smell=W())))
    def sign_5(self):
        self.declare(Fact(gas_smell=input_yes_no("The smell of gasoline is present: ").strip().lower()))


    """
    THE KNOWLEDGE
    """

    @Rule(Fact(action='find_fault'), Fact(headlights_light="yes"), Fact(headlights_dim="no"), Fact(cranks_slowly="no"),
        Fact(gas_smell="no"))
    def fault_1(self):
        self.declare(Fact(fault="Dead Battery"))

    @Rule(Fact(action='find_fault'), Fact(headlights_light="yes"), Fact(headlights_dim="no"), Fact(cranks_slowly="yes"),
        Fact(gas_smell="no"))
    def fault_2(self):
        self.declare(Fact(fault="Empty Gas Tank"))

    @Rule(Fact(action='find_fault'), Fact(headlights_light="yes"), Fact(headlights_dim="yes"), Fact(cranks_slowly="yes"),
        Fact(gas_smell="no"))
    def fault_3(self):
        self.declare(Fact(fault="Battery is weak"))

    @Rule(Fact(action='find_fault'), Fact(headlights_light="yes"), Fact(headlights_dim="no"), Fact(cranks_slowly="no"),
        Fact(gas_smell="yes"))
    def fault_4(self):
        self.declare(Fact(fault="The engine is being flooded with gas"))


    """
    CASE OF UNKOWN FAULT
    """

    @Rule(Fact(action='find_fault'),NOT (Fact(fault = W())),salience = -1)
    def unmatched(self):
        self.declare(Fact(fault = 'unknown'))



    @Rule(Fact(action='find_fault'), Fact(fault=MATCH.fault),salience = -998)
    def display_fault(self, fault):
        print("")
        if fault == 'unknown':
            print(Fore.MAGENTA + f"WE WERE NOT ABLE TO DETERMINE THE ISSUE WITH YOUR VEHICLE\n")
        else:
            print(Fore.MAGENTA + f"{fault.upper()}\n")



		
