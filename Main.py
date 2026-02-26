# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient



def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')] 
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234','Birmingham', ['ChestPain'] ), Patient('Mike','Jones', 37,'07555551234','L2 2AB', 'Liverpool', ['Fever']), Patient('Daivd','Smith', 15, '07123456789','C1 ABC', 'Manchester', ['Cough'])]
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Doctor Management')
        print(' 2- Patient Management')
        print(' 3- Admin Settings')
        print(' 4- Logout')

        # get the option
        op = input('Option: ')

        if op == '1':
            # Doctor Management
            doc_running = True
            while doc_running:
                print('\nDoctor Management:')
                print(' 1- Register Doctor')
                print(' 2- View Doctors')
                print(' 3- Update Doctor')
                print(' 4- Delete Doctor')
                print(' 5- Back to Main Menu')
                
                doc_op = input('Option: ')
                
                if doc_op == '1':
                    admin.doctor_management(doctors)
                elif doc_op == '2':
                    admin.view(doctors)
                elif doc_op == '3':
                    print('Update doctor functionality')
                elif doc_op == '4':
                    print('Delete doctor functionality')
                elif doc_op == '5':
                    doc_running = False
                else:
                    print('Invalid option. Try again')
        
        elif op == '2':
            # Patient Management
            pat_running = True
            while pat_running:
                print('\nPatient Management:')
                print(' 1- View Patients')
                print(' 2- Assign Doctor to Patient')
                print(' 3- Discharge Patient')
                print(' 4- View Discharged Patients')
                print(' 5- View Patient By Family Group')
                print(' 6- Relocate Patient to Another Doctor')
                print(' 7- Back to Main Menu')
                
                pat_op = input('Option: ')
                
                if pat_op == '1':
                    admin.view_patient(patients)
                elif pat_op == '2':
                    admin.assign_doctor_to_patient(patients, doctors)
                elif pat_op == '3':
                    admin.discharge(patients, discharged_patients)
                elif pat_op == '4':
                    admin.view_discharge(discharged_patients)
                elif pat_op == '5':
                    admin.view_family_group(patients)
                elif pat_op == '6':
                    admin.relocate_patients(patients, doctors)
                elif pat_op == '7':
                    pat_running = False
                else:
                    print('Invalid option. Try again')
        
        elif op == '3':
            # Admin Settings
            admin_running = True
            while admin_running:
                print('\nAdmin Settings:')
                print(' 1- Update Admin Details')
                print(' 2- Management Report')
                print(' 3- Back to Main Menu')
                
                admin_op = input('Option: ')
                
                if admin_op == '1':
                    admin.update_details()
                elif admin_op == '2':
                    admin.management_report(patients, doctors)
                elif admin_op == '3':
                    admin_running = False
                else:
                    print('Invalid option. Try again')
        
        elif op == '4':
            # Logout
            running = False
            admin.save_patient_info(patients)
            print('Logging out... ByeBye!')
        
        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
