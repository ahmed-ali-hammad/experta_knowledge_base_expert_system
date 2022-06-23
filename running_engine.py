from base import *

"""
This Knowledge Engine covers the case when the engine starts but still has issues
"""

class RunningCarDiagnosis(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        """
        will be called every time the reset method is called.
        """
        yield Fact(action="find_fault")

    """
    USER INPUT
    """

    @Rule(Fact(action='find_fault'), NOT(Fact(oil_warning_light=W())))
    def sign_1(self):
        self.declare(Fact(oil_warning_light=input_yes_no("Oil pressure warning light is on: ").strip().lower()))

    @Rule(Fact(action='find_fault'), NOT(Fact(sputtering_engine=W())))
    def sign_2(self):
        self.declare(Fact(sputtering_engine=input_yes_no("Is the engine sputtering: ").strip().lower()))

    @Rule(Fact(action='find_fault'), NOT(Fact(shaking_steering_wheel=W())))
    def sign_3(self):
        self.declare(Fact(shaking_steering_wheel=input_yes_no("Is the steering whell shaking: ").strip().lower()))

    @Rule(Fact(action='find_fault'), NOT(Fact(grinding_noise=W())))
    def sign_4(self):
        self.declare(Fact(grinding_noise=input_yes_no("There are grinding noise coming from the wheels: ").strip().lower()))

    @Rule(Fact(action='find_fault'), NOT(Fact(tyres_wearing_unevenly=W())))
    def sign_5(self):
        self.declare(Fact(tyres_wearing_unevenly=input_yes_no("The tyres are wearing unevenly: ").strip().lower()))

    @Rule(Fact(action='find_fault'), NOT(Fact(consuming_too_much_oil=W())))
    def sign_6(self):
        self.declare(Fact(consuming_too_much_oil=input_yes_no("The car is consuming too much oil: ").strip().lower()))

    @Rule(Fact(action='find_fault'), NOT(Fact(temperature_warning_light=W())))
    def sign_7(self):
        self.declare(Fact(temperature_warning_light=input_yes_no("The temperature warning light is on: ").strip().lower()))

    @Rule(Fact(action='find_fault'), NOT(Fact(excessive_emissions=W())))
    def sign_8(self):
        self.declare(Fact(excessive_emissions=input_yes_no("The car gives out excessive emissions: ").strip().lower()))

    @Rule(Fact(action='find_fault'), NOT(Fact(slipping_transmission=W())))
    def sign_9(self):
        self.declare(Fact(slipping_transmission=input_yes_no("Transmission is slipping: ").strip().lower()))



    """
    THE KNOWLEDGE
    """

    @Rule(Fact(action='find_fault'), Fact(oil_warning_light="yes"))
    def fault_1(self):
        self.declare(Fact(fault="The engine is leaking oil, the car mustn't be driven"))

    @Rule(Fact(action='find_fault'), Fact(sputtering_engine="yes"))
    def fault_2(self):
        self.declare(Fact(fault="fuel and ignition systems need to be maintained"))

    @Rule(Fact(action='find_fault'), Fact(shaking_steering_wheel="yes"))
    def fault_3(self):
        self.declare(Fact(fault="Suspension system needs to be maintained"))

    @Rule(Fact(action='find_fault'), Fact(grinding_noise="yes"))
    def fault_4(self):
        self.declare(Fact(fault="Breaks are worn out and need to be replaced"))

    @Rule(Fact(action='find_fault'), Fact(tyres_wearing_unevenly="yes"))
    def fault_5(self):
        self.declare(Fact(fault="Suspension needs alignment"))

    @Rule(Fact(action='find_fault'), Fact(consuming_too_much_oil="yes"))
    def fault_6(self):
        self.declare(Fact(fault="Damaged gaskets, oil leakage, or piston rings"))

    @Rule(Fact(action='find_fault'), Fact(temperature_warning_light="yes"))
    def fault_7(self):
        self.declare(Fact(fault="An issue with the cooling system, the car mustn't be driven"))

    @Rule(Fact(action='find_fault'), Fact(excessive_emissions="yes"))
    def fault_8(self):
        self.declare(Fact(fault="O2 sensor might be faulty"))

    @Rule(Fact(action='find_fault'), Fact(slipping_transmission="yes"))
    def fault_9(self):
        self.declare(Fact(fault="damage or clogging in the seals, gaskets and lines inside the transmission"))


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

