from Doctor import Doctor
from Patient import Patient
from Person import Person
from Appointment import Appointment



class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')
        
        # checks if the username and password is entered 
        if len(username) == 0 and len(password)==0:
            print("Please enter the username and password")
        # check if the username and password match the registered ones
        if username == 'admin' and password == '123':
            print("Login Successful")
        
        return self.__username == username and self.__password == password

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True
        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #Details of the doctor from the user
        first_name = input("Enters the doctor's first name:")
        surname = input("Enter the doctor's surname: ")
        speciality = input("enter the doctor's speciality: ")
        return first_name, surname, speciality

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----") 

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        
        op = input('Option:')

        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4
            first_name, surname, speciality = self.get_doctor_details()


            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    name_exists = True
                    break # save time and end the loop
                    
            if not name_exists:
                new_doctor = Doctor(first_name,surname,speciality)
                doctors.append(new_doctor) # add the doctor ...
                                                         # ... to the list of doctors
            
                
                print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            print('ID |          Full name           |  Speciality')
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1 # doctor_index is the ID minus one (-1)
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                        print("Doctor found")
                        break
                        
                    else:
                        print("Doctor not found")            
                    #printing updated list of doctors
                    self.view(doctors)
                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: ')) # make the user input lowercase

            #ToDo8
            if op ==1:
                new_first_name = input('Enter doctor`s new first name: ')
                doctors[doctor_index].set_first_name(new_first_name)
            elif op ==2 :
                new_surname = input("Enter doctor`s new surname: ")
                doctors[doctor_index].set_surname(new_surname)
            elif op == 3:
                new_speciality = input("Enter doctor`s new speciality: ")
                doctors[doctor_index].set_speciality(new_speciality)

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = input('Enter the ID of the doctor to be deleted: ')
            #ToDo9
            if len(doctor_index) == 0:
                print('Enter doctor Id')
            else:
                try:
                    doctor_index = int(doctor_index) -1
                    if doctor_index in range(len(doctors)):
                        del doctors[doctor_index]
                        print("Doctor deleted")
                    else:
                        print('The id entered was not found')

                except ValueError: # the entered id could not be changed into an int
                    print('The id entered is incorrect')

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |       Address      |      Symptoms    |')
        print('-'*143)


        #ToDo10
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |       Address      |      Symptoms    |')
        print('-'*143)


        self.view(patients)

        patient_index = input('Please enter the patient ID: ')
        

        try:
            # patient_index is the patient ID minus one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID minus one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                patients[patient_index] . link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index])
                date = input("Enter appointment month: ")
                appointment = Appointment(patients[patient_index], date)
                doctors[doctor_index].add_appointment(appointment)
                
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        # prints a list of all patients and ask user if they wanna discharge
        print("-----Discharge Patient-----")

        self.view_patient(patients)

        while True:
            choice = input('Do you want the patient to be discharged(Y/N: ')
            if choice.upper() == 'Y'or choice.upper() == 'YES':

                patient_index = input('Please enter the patient ID: ')

                #ToDo12
                try:
                    patient_index = int(patient_index)-1
                    if patient_index not in range(len(patients)):
                        print("Patient Id was not found")
                    else:
                        discharged_patient = patients.pop(patient_index)
                        discharge_patients.append(discharged_patient)
                        print("The patient is successfully discharged")
                except ValueError: # the entered id could not be changed into an int
                    print('The id entered is incorrect')
            if choice.upper()=='N'or choice.upper()=='NO':
                break
                

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |       Address      |      Symptoms    |')
        print('-'*143)
        
        self.view(discharged_patients)

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            #ToDo14
            username = input('Enter the new username: ')
            self.__username = username

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password

        elif op == 3:
            #ToDo15
            address = input('Enter the new address:')
            self.__address = address
            

        else:
            #ToDo16
            print('Invalid operation choosen. Check your spelling!')

    
    def view_family_group(self,patients):
        print("-----View Family Group-----")
        surname = input('Enter the family surname: ')
        
        family_members = [] #storing family members in a list
        for patient in patients:
            if patient.get_surname() == surname:
                family_members.append(patient)


        #making sure family members exist
        if len(family_members) == 0:
            print("No patients for this family")
        else:
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |       Address      |      Symptoms    |')
            print('-'*143)

            self.view(family_members)



    #relocating patients from one doctor to another
    def relocate_patients(self, patients,doctors):
        print("-----Relocate Patients-----")
        previous_doctor = input("Enter current doctor's fullname: ")
        new_doctor = input("Enter new doctor's fullname: ")

        count = 0
        for patient in patients:
            if patient.get_doctor() == previous_doctor:
                patient.link(new_doctor)
                count +=1
        if count == 0:
            print("No patients found for this doctor")
        else:
            print(f"{count} patients have been relocated from Dr. {previous_doctor} to Dr. {new_doctor}")

    
    #management report

    def management_report(self, patients, doctors):
        print("-----Management Report-----")
        print(f'The total number of doctors in the system is {len(doctors)}')
        print("\n Patients per Doctor")
        for doctor in doctors:
            count_patients = len(doctor.get_patients())
            print(f'The total number of patients for Dr.{doctor.full_name()} : {count_patients}')

        print("\nTotal appointments per month per doctor")
        for doctor in doctors:
            appointments = doctor.get_appointments()
            #checking appointment exists
            if len(appointments) == 0:
                print("There are no any appointments")

            else:
                months = []
                for appnmt in appointments:
                    months.append(appnmt.get_date())

                for month in set(months):  #set doesnot use duplicate value 
                    print(f'{month}: {months.count(month)} appointments for Dr. {doctor.full_name()}')
        
        print("\nTotal number of patient based on ilness type")
        count_illness = {}
        for patient in patients:
            for illness in patient.get_symptoms():
                if illness in count_illness:
                    count_illness[illness] +=1
                else:
                    count_illness[illness] = 1
        for illness in count_illness:
            print(illness, count_illness[illness])
        
        
        # file handleing

    #saving patient information in a file
    def save_patient_info(self,patients):
        filename = 'patients.txt'
        try:
            with open(filename,'w') as file:
                file.write("Firstname, Surname, Doctor, Age, Mobile, Postcode, Address, Symptoms\n")
                for patient in patients:
                    symptoms = ';'.join(patient.get_symptoms()) if patient.get_symptoms() else 'None'
                    file.write(f'{patient.get_first_name()},{patient.get_surname()},{patient.get_doctor()},{patient.get_age()},{patient.get_mobile()},{patient.get_postcode()},{patient.get_address()},{symptoms}\n')
                    print("Patient information is successfully saved.")
        except FileNotFoundError:
            print("Error: The file was not found.")
    
    #loading patient information from a file
    def get_patient_info(self):
        patients = []
        filename = 'patients.txt'
        try:
            with open(filename,'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    first_name, surname, age, mobile, postcode, address, doctor, symptoms = data
                    patient = Patient(first_name, surname, int(age), mobile, postcode, address, symptoms)
                    patient.link(doctor)
                    patients.append(patient)
            print("Patient information is successfully loaded.")
        except FileNotFoundError:
            print("Error: The file was not found.")
        return patients
  

                   


        
        
        

    
     

        
    

     
   





