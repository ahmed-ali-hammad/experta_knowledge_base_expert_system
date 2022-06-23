from non_running_engine import *
from running_engine import *

if __name__ == "__main__":
    print(Fore.YELLOW + welcome_message)
    while(1):
        print(Fore.WHITE)
        expert_select = input('\nDoes the engine start?\n\n').strip().lower()
        if expert_select == 'no':
            knowledge_engine = NonRunningCarDiagnosis()
            knowledge_engine.reset()  # Prepare the engine for the execution.
            knowledge_engine.run()  # Run it!
        elif expert_select == 'yes':
            knowledge_engine = RunningCarDiagnosis()
            knowledge_engine.reset()  # Prepare the engine for the execution.
            knowledge_engine.run()  # Run it!
        else:
            print('\nNO VALID ANSWER SELECTED\n')
            continue

        if input_yes_no('Would you like to diagnose other vechilcs?').strip().lower() == "no":
            print(Fore.YELLOW + '\n\nThank you for using our Car Diagnosis Expert System\n\n')
            exit()
