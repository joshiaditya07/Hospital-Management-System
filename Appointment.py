
class Appointment:
    def __init__(self, patient,date):
        self.__patient = patient
        self.__date = date

    def get_date(self):
        return self.__date
    
    def get_patient(self):
        return self.__patient