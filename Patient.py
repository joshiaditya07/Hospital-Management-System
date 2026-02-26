from Person import Person

class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode,address,symptoms):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        
        #ToDo1-  Initializing the attributes
        super().__init__(first_name, surname)
        self.__age = age
        self.__mobile = mobile 
        self.__postcode = postcode
        self.__address = address
        self.__doctor = 'None'
        self.__symptoms = symptoms
        
    def get_doctor(self) :
        #ToDo3 - returns the doctor of the patient
        return self.__doctor

    def get_address(self):
        return self.__address
    
    def get_mobile(self):
        return self.__mobile
    
    def get_age(self):
        return self.__age
    
    def get_postcode(self):
        return self.__postcode 

    def get_symptoms(self):
        return self.__symptoms

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        #ToDo4
        for symptom in self.__symptoms:
            print(symptom)
        

    def __str__(self):
        symptoms = ', '.join(self.__symptoms) if self.__symptoms else 'None'
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}|{self.__address:^20}|{symptoms:^20}|'
