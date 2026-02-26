import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
from Appointment import Appointment
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class HospitalManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("900x700")
        
        # Initialize data
        self.admin = Admin('admin', '123', 'B1 1AB')
        
        self.doctors = [
            Doctor('John', 'Smith', 'Internal Med.'),
            Doctor('Jone', 'Smith', 'Pediatrics'),
            Doctor('Jone', 'Carlos', 'Cardiology')
        ]
        self.patients = [
            Patient('Sara', 'Smith', 20, '07012345678', 'B1 234', 'Birmingham',['ChestPain']),
            Patient('Mike', 'Jones', 37, '07555551234', 'L2 2AB', 'Liverpool',['Fever']),
            Patient('Daivd', 'Smith', 15, '07123456789', 'C1 ABC', 'Manchester',['Cough'])
        ]
        self.discharged_patients = []
        self.logged_in = False
        
        self.show_login_window()
    
    def show_login_window(self):
        """Login window"""
        self.clear_window()
        
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True)
        
        ttk.Label(frame, text="Hospital Management System", font=("Arial", 20, "bold")).pack(pady=20)
        ttk.Label(frame, text="Login", font=("Arial", 16, "bold")).pack(pady=10)
        
        ttk.Label(frame, text="Username:").pack(pady=5)
        username_entry = ttk.Entry(frame, width=30)
        username_entry.pack(pady=5)
        
        ttk.Label(frame, text="Password:").pack(pady=5)
        password_entry = ttk.Entry(frame, width=30, show="*")
        password_entry.pack(pady=5)
        
        def login():
            username = username_entry.get()
            password = password_entry.get()
            
            if username == 'admin' and password == '123':
                self.logged_in = True
                messagebox.showinfo("Login Successful", "You have successfully logged in!")
                self.show_main_menu()
            else:
                messagebox.showerror("Login Failed", "Incorrect username or password.")
        
        ttk.Button(frame, text="Login", command=login).pack(pady=20)
    
    def clear_window(self):
        """Clear window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_main_menu(self):
        """Main menu"""
        self.clear_window()
        
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Hospital Management System", font=("Arial", 18, "bold")).pack(pady=10)
        ttk.Label(frame, text="Main Menu", font=("Arial", 14, "bold")).pack(pady=10)
        
        button_frame = ttk.Frame(frame)
        button_frame.pack(pady=20)
        
        buttons = [
            ("Doctor Management", self.show_doctor_menu),
            ("Patient Management", self.show_patient_menu),
            ("Admin Settings", self.show_admin_menu),
            ("Logout", self.logout)
        ]
        
        for text, command in buttons:
            ttk.Button(button_frame, text=text, command=command, width=40).pack(pady=10)
    
    def show_doctor_menu(self):
        """Doctor management menu"""
        self.clear_window()
        
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Hospital Management System", font=("Arial", 18, "bold")).pack(pady=10)
        ttk.Label(frame, text="Doctor Management", font=("Arial", 14, "bold")).pack(pady=10)
        
        button_frame = ttk.Frame(frame)
        button_frame.pack(pady=20)
        
        buttons = [
            ("Register Doctor", self.register_doctor),
            ("View Doctors", self.view_doctors),
            ("Update Doctor", self.update_doctor),
            ("Delete Doctor", self.delete_doctor),
            ("Back to Main Menu", self.show_main_menu)
        ]
        
        for text, command in buttons:
            ttk.Button(button_frame, text=text, command=command, width=40).pack(pady=5)
    
    def show_patient_menu(self):
        """Patient management menu"""
        self.clear_window()
        
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Hospital Management System", font=("Arial", 18, "bold")).pack(pady=10)
        ttk.Label(frame, text="Patient Management", font=("Arial", 14, "bold")).pack(pady=10)
        
        button_frame = ttk.Frame(frame)
        button_frame.pack(pady=20)
        
        buttons = [
            ("View Patients", self.show_view_patients),
            ("Assign Doctor to Patient", self.show_assign_doctor),
            ("Discharge Patient", self.show_discharge_window),
            ("View Discharged Patients", self.show_discharged_patients),
            ("View Patient By Family Group", self.show_family_group),
            ("Relocate Patient to Another Doctor", self.show_relocate_patients),
            ("Back to Main Menu", self.show_main_menu)
        ]
        
        for text, command in buttons:
            ttk.Button(button_frame, text=text, command=command, width=40).pack(pady=5)
    
    def show_admin_menu(self):
        """Admin settings menu"""
        self.clear_window()
        
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Hospital Management System", font=("Arial", 18, "bold")).pack(pady=10)
        ttk.Label(frame, text="Admin Settings", font=("Arial", 14, "bold")).pack(pady=10)
        
        button_frame = ttk.Frame(frame)
        button_frame.pack(pady=20)
        
        buttons = [
            ("Update Admin Details", self.show_update_admin),
            ("Management Report", self.show_management_report),
            ("Back to Main Menu", self.show_main_menu)
        ]
        
        for text, command in buttons:
            ttk.Button(button_frame, text=text, command=command, width=40).pack(pady=5)
    
    def register_doctor(self):
        """Register doctor"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Register Doctor")
        dialog.geometry("400x250")
        
        ttk.Label(dialog, text="Register Doctor", font=("Arial", 14, "bold")).pack(pady=10)
        
        ttk.Label(dialog, text="First Name:").pack(pady=5)
        first_name_entry = ttk.Entry(dialog, width=30)
        first_name_entry.pack(pady=5)
        
        ttk.Label(dialog, text="Surname:").pack(pady=5)
        surname_entry = ttk.Entry(dialog, width=30)
        surname_entry.pack(pady=5)
        
        ttk.Label(dialog, text="Speciality:").pack(pady=5)
        speciality_entry = ttk.Entry(dialog, width=30)
        speciality_entry.pack(pady=5)
        
        def save_doctor():
            first_name = first_name_entry.get().strip()
            surname = surname_entry.get().strip()
            speciality = speciality_entry.get().strip()
            
            if not first_name or not surname or not speciality:
                messagebox.showerror("Error", "All fields are required.")
                return
            
            name_exists = False
            for doctor in self.doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    name_exists = True
                    break
            
            if name_exists:
                messagebox.showerror("Error", "Doctor already exists.")
            else:
                new_doctor = Doctor(first_name, surname, speciality)
                self.doctors.append(new_doctor)
                messagebox.showinfo("Success", "Doctor registered successfully.")
                dialog.destroy()
        
        ttk.Button(dialog, text="Register", command=save_doctor).pack(pady=10)
    
    def view_doctors(self):
        """View doctors"""
        dialog = tk.Toplevel(self.root)
        dialog.title("View Doctors")
        dialog.geometry("700x400")
        
        ttk.Label(dialog, text="List of Doctors", font=("Arial", 14, "bold")).pack(pady=10)
        
        text_widget = scrolledtext.ScrolledText(dialog, width=85, height=15, state=tk.DISABLED, font=("Courier", 10))
        text_widget.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        text_widget.config(state=tk.NORMAL)
        text_widget.insert(tk.END, f"{'ID':<5} | {'Full Name':<25} | {'Speciality':<35}\n")
        text_widget.insert(tk.END, "-" * 70 + "\n")
        
        for index, doctor in enumerate(self.doctors):
            text_widget.insert(tk.END, f"{index+1:<5} | {doctor.full_name():<25} | {doctor.get_speciality():<35}\n")
        
        text_widget.config(state=tk.DISABLED)
        ttk.Button(dialog, text="Close", command=dialog.destroy).pack(pady=10)
    
    def show_view_patients(self):
        """View patients"""
        dialog = tk.Toplevel(self.root)
        dialog.title("View Patients")
        dialog.geometry("1300x500")
        
        ttk.Label(dialog, text="List of Patients", font=("Arial", 14, "bold")).pack(pady=10)
        
        text_widget = scrolledtext.ScrolledText(
            dialog, width=160, height=15, state=tk.DISABLED, font=("Courier", 9)
        )
        text_widget.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        text_widget.config(state=tk.NORMAL)
        
        
        text_widget.insert(
            tk.END,
            f"{'ID':<5} | {'Full Name':<20} | {'Doctor Name':<20} | "
            f"{'Age':<5} | {'Mobile':<15} | {'Postcode':<12} | "
            f"{'Address':<15} | {'Symptoms'}\n"
        )
        text_widget.insert(tk.END, "-" * 160 + "\n")
        
        if not self.patients:
            text_widget.insert(tk.END, "No patients available.\n")
        else:
            for index, patient in enumerate(self.patients):
                symptoms = ", ".join(patient.get_symptoms()) if patient.get_symptoms() else "None"
                
                text_widget.insert(
                    tk.END,
                    f"{index+1:<5} | {patient.full_name():<20} | "
                    f"{patient.get_doctor():<20} | {patient.get_age():<5} | "
                    f"{patient.get_mobile():<15} | {patient.get_postcode():<12} | "
                    f"{patient.get_address():<15} | {symptoms}\n"
                )
        
        text_widget.config(state=tk.DISABLED)
        ttk.Button(dialog, text="Close", command=dialog.destroy).pack(pady=10)

    def update_doctor(self):
        """Update doctor"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Update Doctor")
        dialog.geometry("500x300")
        
        ttk.Label(dialog, text="Update Doctor Details", font=("Arial", 14, "bold")).pack(pady=10)
        
        ttk.Label(dialog, text="Select Doctor ID:").pack(pady=5)
        doctor_id_var = tk.StringVar()
        doctor_combo = ttk.Combobox(dialog, textvariable=doctor_id_var, width=27)
        doctor_options = [f"{i+1} - {self.doctors[i].full_name()}" for i in range(len(self.doctors))]
        doctor_combo['values'] = doctor_options
        doctor_combo.pack(pady=5)
        
        ttk.Label(dialog, text="Select Field to Update:").pack(pady=5)
        field_var = tk.StringVar(value="First Name")
        field_combo = ttk.Combobox(dialog, textvariable=field_var, values=["First Name", "Surname", "Speciality"], state="readonly", width=27)
        field_combo.pack(pady=5)
        
        ttk.Label(dialog, text="New Value:").pack(pady=5)
        new_value_entry = ttk.Entry(dialog, width=30)
        new_value_entry.pack(pady=5)
        
        def update():
            try:
                doctor_id = int(doctor_id_var.get().split()[0]) - 1
                new_value = new_value_entry.get().strip()
                field = field_var.get()
                
                if not new_value:
                    messagebox.showerror("Error", "New value cannot be empty.")
                    return
                
                if field == "First Name":
                    self.doctors[doctor_id].set_first_name(new_value)
                elif field == "Surname":
                    self.doctors[doctor_id].set_surname(new_value)
                elif field == "Speciality":
                    self.doctors[doctor_id].set_speciality(new_value)
                
                messagebox.showinfo("Success", "Doctor updated successfully.")
                dialog.destroy()
            except:
                messagebox.showerror("Error", "Invalid selection.")
        
        ttk.Button(dialog, text="Update", command=update).pack(pady=10)
    
    def delete_doctor(self):
        """Delete doctor"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Delete Doctor")
        dialog.geometry("400x200")
        
        ttk.Label(dialog, text="Delete Doctor", font=("Arial", 14, "bold")).pack(pady=10)
        
        ttk.Label(dialog, text="Select Doctor ID:").pack(pady=5)
        doctor_id_var = tk.StringVar()
        doctor_combo = ttk.Combobox(dialog, textvariable=doctor_id_var, width=27)
        doctor_options = [f"{i+1} - {self.doctors[i].full_name()}" for i in range(len(self.doctors))]
        doctor_combo['values'] = doctor_options
        doctor_combo.pack(pady=5)
        
        def delete():
            try:
                doctor_id = int(doctor_id_var.get().split()[0]) - 1
                if messagebox.askyesno("Confirm", f"Delete Dr. {self.doctors[doctor_id].full_name()}?"):
                    del self.doctors[doctor_id]
                    messagebox.showinfo("Success", "Doctor deleted successfully.")
                    dialog.destroy()
            except:
                messagebox.showerror("Error", "Invalid selection.")
        
        ttk.Button(dialog, text="Delete", command=delete).pack(pady=10)
    
    def show_assign_doctor(self):
        """Assign doctor"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Assign Doctor to Patient")
        dialog.geometry("600x500")
        
        ttk.Label(dialog, text="Assign Doctor to Patient", font=("Arial", 14, "bold")).pack(pady=10)
        
        ttk.Label(dialog, text="Select Patient:").pack(pady=5)
        patient_id_var = tk.StringVar()
        patient_combo = ttk.Combobox(dialog, textvariable=patient_id_var, width=50)
        patient_options = [f"{i+1} - {self.patients[i].full_name()} ({','.join (self.patients[i].get_symptoms())})" for i in range(len(self.patients))]
        patient_combo['values'] = patient_options
        patient_combo.pack(pady=5)
        
        ttk.Label(dialog, text="Select Doctor:").pack(pady=5)
        doctor_id_var = tk.StringVar()
        doctor_combo = ttk.Combobox(dialog, textvariable=doctor_id_var, width=50)
        doctor_options = [f"{i+1} - {self.doctors[i].full_name()} ({self.doctors[i].get_speciality()})" for i in range(len(self.doctors))]
        doctor_combo['values'] = doctor_options
        doctor_combo.pack(pady=5)
        
        ttk.Label(dialog, text="Appointment Month:").pack(pady=5)
        month_entry = ttk.Entry(dialog, width=50)
        month_entry.pack(pady=5)
        
        def assign():
            try:
                patient_idx = int(patient_id_var.get().split()[0]) - 1
                doctor_idx = int(doctor_id_var.get().split()[0]) - 1
                month = month_entry.get().strip()
                
                if not month:
                    messagebox.showerror("Error", "Appointment Month is required")
                    return
                

                self.patients[patient_idx].link(self.doctors[doctor_idx].full_name())
                self.doctors[doctor_idx].add_patient(self.patients[patient_idx])
                
                appointment = Appointment(self.patients[patient_idx], month)
                self.doctors[doctor_idx].add_appointment(appointment)
                
                messagebox.showinfo("Success", "Patient assigned to doctor successfully.")
                dialog.destroy()
            except:
                messagebox.showerror("Error", "Invalid selection.")
        
        ttk.Button(dialog, text="Assign", command=assign).pack(pady=10)
    
    def show_discharge_window(self):
        """Discharge patient"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Discharge Patient")
        dialog.geometry("1150x500")
        
        ttk.Label(dialog, text="Discharge Patient", font=("Arial", 14, "bold")).pack(pady=10)
        
        text_widget = scrolledtext.ScrolledText(dialog, width=140, height=13, state=tk.DISABLED, font=("Courier", 9))
        text_widget.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        text_widget.config(state=tk.NORMAL)
        text_widget.insert(tk.END, f"{'ID':<5} | {'Full Name':<20} | {'Doctor Name':<20} | {'Age':<5} | {'Mobile':<15} | {'Postcode':<12} | {'Address':<15} | {'Symptoms'}\n")
        text_widget.insert(tk.END, "-" * 135 + "\n")
        
        for index, patient in enumerate(self.patients):
            symptoms= ', '.join(patient.get_symptoms()) if patient.get_symptoms() else 'None'
            text_widget.insert(tk.END, f"{index+1:<5} | {patient.full_name():<20} | {patient.get_doctor():<20} | {patient.get_age():<5} | {patient.get_mobile():<15} | {patient.get_postcode():<12} | {patient.get_address():<15} | {symptoms}\n")
        
        text_widget.config(state=tk.DISABLED)
        
        ttk.Label(dialog, text="Patient ID to Discharge:").pack(pady=5)
        patient_id_var = tk.StringVar()
        patient_id_entry = ttk.Entry(dialog, textvariable=patient_id_var, width=30)
        patient_id_entry.pack(pady=5)
        
        def discharge():
            try:
                patient_id = int(patient_id_var.get()) - 1
                if patient_id not in range(len(self.patients)):
                    messagebox.showerror("Error", "Patient ID not found.")
                    return
                
                if messagebox.askyesno("Confirm", f"Discharge {self.patients[patient_id].full_name()}?"):
                    discharged_patient = self.patients.pop(patient_id)
                    self.discharged_patients.append(discharged_patient)
                    messagebox.showinfo("Success", "Patient discharged successfully.")
                    dialog.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid patient ID.")
        
        ttk.Button(dialog, text="Discharge", command=discharge).pack(pady=10)
    
    def show_discharged_patients(self):
        """View discharged patients"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Discharged Patients")
        dialog.geometry("1150x500")
        
        ttk.Label(dialog, text="Discharged Patients", font=("Arial", 14, "bold")).pack(pady=10)
        
        text_widget = scrolledtext.ScrolledText(dialog, width=140, height=15, state=tk.DISABLED, font=("Courier", 9))
        text_widget.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        text_widget.config(state=tk.NORMAL)
        text_widget.insert(tk.END, f"{'ID':<5} | {'Full Name':<20} | {'Doctor Name':<20} | {'Age':<5} | {'Mobile':<15} | {'Postcode':<12} | {'Address':<35}\n")
        text_widget.insert(tk.END, "-" * 135 + "\n")
        
        if not self.discharged_patients:
            text_widget.insert(tk.END, "No discharged patients.\n")
        else:
            for index, patient in enumerate(self.discharged_patients):
                text_widget.insert(tk.END, f"{index+1:<5} | {patient.full_name():<20} | {patient.get_doctor():<20} | {patient.get_age():<5} | {patient.get_mobile():<15} | {patient.get_postcode():<12} | {patient.get_address():<35}\n")
        
        text_widget.config(state=tk.DISABLED)
        ttk.Button(dialog, text="Close", command=dialog.destroy).pack(pady=10)
    
    def show_family_group(self):
        """View family group"""
        dialog = tk.Toplevel(self.root)
        dialog.title("View Patient By Family Group")
        dialog.geometry("1150x500")
        
        ttk.Label(dialog, text="View Patient By Family Group", font=("Arial", 14, "bold")).pack(pady=10)
        
        ttk.Label(dialog, text="Enter Family Surname:").pack(pady=5)
        surname_entry = ttk.Entry(dialog, width=30)
        surname_entry.pack(pady=5)
        
        text_widget = scrolledtext.ScrolledText(dialog, width=140, height=15, state=tk.DISABLED, font=("Courier", 9))
        text_widget.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        def search():
            text_widget.config(state=tk.NORMAL)
            text_widget.delete(1.0, tk.END)
            
            surname = surname_entry.get().strip()
            if not surname:
                messagebox.showerror("Error", "Please enter a surname.")
                return
           
            family_members = [p for p in self.patients if p.get_surname() == surname]
                
            if not family_members:
                    text_widget.insert(tk.END, "No patients found for this family.\n")
            else:
                text_widget.insert(tk.END, f"{'ID':<5} | {'Full Name':<20} | {'Doctor Name':<20} | {'Age':<5} | {'Mobile':<15} | {'Postcode':<12} | {'Address':<15} | {'Symptoms'}\n")
                text_widget.insert(tk.END, "-" * 135 + "\n")
                for index, patient in enumerate(family_members):
                    symptoms = ", ".join(patient.get_symptoms()) if patient.get_symptoms() else "None"
                    text_widget.insert(tk.END, f"{index+1:<5} | {patient.full_name():<20} | {patient.get_doctor():<20} | {patient.get_age():<5} | {patient.get_mobile():<15} | {patient.get_postcode():<12} | {patient.get_address():<15} | {symptoms}\n")
            
            text_widget.config(state=tk.DISABLED)
        
        ttk.Button(dialog, text="Search", command=search).pack(pady=5)
    
    def show_relocate_patients(self):
        """Relocate patient"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Relocate Patient")
        dialog.geometry("500x250")
        
        ttk.Label(dialog, text="Relocate Patient to Another Doctor", font=("Arial", 14, "bold")).pack(pady=10)
        
        ttk.Label(dialog, text="Current Doctor's Full Name:").pack(pady=5)
        current_doctor_entry = ttk.Entry(dialog, width=35)
        current_doctor_entry.pack(pady=5)
        
        ttk.Label(dialog, text="New Doctor's Full Name:").pack(pady=5)
        new_doctor_entry = ttk.Entry(dialog, width=35)
        new_doctor_entry.pack(pady=5)
        
        def relocate():
            current_doctor = current_doctor_entry.get().strip()
            new_doctor = new_doctor_entry.get().strip()
            
            if not current_doctor or not new_doctor:
                messagebox.showerror("Error", "Both fields are required.")
                return
            
            count = 0
            for patient in self.patients:
                if patient.get_doctor() == current_doctor:
                    patient.link(new_doctor)
                    count += 1
            
            if count == 0:
                messagebox.showwarning("Info", "No patients found for this doctor.")
            else:
                messagebox.showinfo("Success", f"{count} patients have been relocated from Dr. {current_doctor} to Dr. {new_doctor}")
                dialog.destroy()
        
        ttk.Button(dialog, text="Relocate", command=relocate).pack(pady=10)
    
    def show_update_admin(self):
        """Update admin"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Update Admin Details")
        dialog.geometry("400x250")
        
        ttk.Label(dialog, text="Update Admin Details", font=("Arial", 14, "bold")).pack(pady=10)
        
        ttk.Label(dialog, text="Select Field to Update:").pack(pady=5)
        field_var = tk.StringVar(value="Username")
        field_combo = ttk.Combobox(dialog, textvariable=field_var, values=["Username", "Password", "Address"], state="readonly", width=30)
        field_combo.pack(pady=5)
        
        ttk.Label(dialog, text="New Value:").pack(pady=5)
        new_value_entry = ttk.Entry(dialog, width=30)
        new_value_entry.pack(pady=5)
        
        def update():
            field = field_var.get()
            new_value = new_value_entry.get().strip()
            
            if not new_value:
                messagebox.showerror("Error", "New value cannot be empty.")
                return
            
            if field == "Username":
                self.admin._Admin__username = new_value
                messagebox.showinfo("Success", "Username updated successfully.")
            elif field == "Password":
                self.admin._Admin__password = new_value
                messagebox.showinfo("Success", "Password updated successfully.")
            elif field == "Address":
                self.admin._Admin__address = new_value
                messagebox.showinfo("Success", "Address updated successfully.")
            
            dialog.destroy()
        
        ttk.Button(dialog, text="Update", command=update).pack(pady=10)
    
    def show_management_report(self):
        """Management report"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Management Report")
        dialog.geometry("900x700")
        
        ttk.Label(dialog, text="Management Report", font=("Arial", 14, "bold")).pack(pady=10)
        
        button_frame = ttk.Frame(dialog)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="View Text Report", command=lambda: self.show_text_report(dialog)).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="View All Charts", command=lambda: self.show_all_charts(dialog)).pack(side=tk.LEFT, padx=5)
        
        # Create a frame for displaying content
        self.report_frame = ttk.Frame(dialog)
        self.report_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Show text report by default
        self.show_text_report(dialog)
    
    def clear_report_frame(self):
        """Clear chart display"""
        for widget in self.report_frame.winfo_children():
            widget.destroy()
    
    def show_text_report(self, dialog):
        """Text report"""
        self.clear_report_frame()
        
        text_widget = scrolledtext.ScrolledText(self.report_frame, width=100, height=30, state=tk.DISABLED)
        text_widget.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        text_widget.config(state=tk.NORMAL)
        
        text_widget.insert(tk.END, f"Total number of doctors in the system: {len(self.doctors)}\n\n")
        
        text_widget.insert(tk.END, "Patients per Doctor:\n")
        text_widget.insert(tk.END, "-" * 50 + "\n")
        for doctor in self.doctors:
            count_patients = len(doctor.get_patients())
            text_widget.insert(tk.END, f"Dr. {doctor.full_name()}: {count_patients} patients\n")
        
        text_widget.insert(tk.END, "\nAppointments per Month per Doctor:\n")
        text_widget.insert(tk.END, "-" * 50 + "\n")
        for doctor in self.doctors:
            appointments = doctor.get_appointments()
            if len(appointments) == 0:
                text_widget.insert(tk.END, f"Dr. {doctor.full_name()}: No appointments\n")
            else:
                months = [appnmt.get_date() for appnmt in appointments]
                for month in set(months):
                    text_widget.insert(tk.END, f"{month}: {months.count(month)} appointments for Dr. {doctor.full_name()}\n")
        
        text_widget.insert(tk.END, "\nPatients by Illness Type:\n")
        text_widget.insert(tk.END, "-" * 50 + "\n")
        count_illness = {}
        all_patients = self.patients + self.discharged_patients
        for patient in all_patients:
            for illness in patient.get_symptoms():
                count_illness[illness] = count_illness.get(illness, 0) + 1
        
        if not count_illness:
            text_widget.insert(tk.END, "No illness data recorded.\n")
        else:
            for illness, count in count_illness.items():
                text_widget.insert(tk.END, f"{illness}: {count} patients\n")
        
        text_widget.config(state=tk.DISABLED)
    
    def show_doctors_chart(self, dialog):
        """Total doctors chart"""
        self.clear_report_frame()
        
        fig = Figure(figsize=(8, 5), dpi=100)
        ax = fig.add_subplot(111)
        
        total_doctors = len(self.doctors)
        ax.bar(['Total Doctors'], [total_doctors], color='steelblue', width=0.5)
        ax.set_ylabel('Count')
        ax.set_title('Total Number of Doctors in the System')
        ax.set_ylim(0, max(total_doctors + 2, 5))
        
        for i, v in enumerate([total_doctors]):
            ax.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold')
        
        canvas = FigureCanvasTkAgg(fig, master=self.report_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def show_patients_per_doctor_chart(self, dialog):
        """Patients per doctor chart"""
        self.clear_report_frame()
        
        fig = Figure(figsize=(10, 5), dpi=100)
        ax = fig.add_subplot(111)
        
        doctor_names = [f"Dr. {d.full_name()}" for d in self.doctors]
        patient_counts = [len(d.get_patients()) for d in self.doctors]
        
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
        ax.bar(doctor_names, patient_counts, color=colors[:len(self.doctors)], width=0.6)
        ax.set_ylabel('Number of Patients')
        ax.set_title('Total Number of Patients per Doctor')
        ax.set_ylim(0, max(patient_counts + [2]))
        
        for i, v in enumerate(patient_counts):
            ax.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold')
        
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
        fig.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, master=self.report_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def show_appointments_chart(self, dialog):
        """Appointments chart"""
        self.clear_report_frame()
        
        fig = Figure(figsize=(12, 6), dpi=100)
        ax = fig.add_subplot(111)
        
        appointments_data = {}
        for doctor in self.doctors:
            appointments = doctor.get_appointments()
            if appointments:
                months = [appnmt.get_date() for appnmt in appointments]
                for month in set(months):
                    key = f"{month} - Dr. {doctor.full_name()}"
                    appointments_data[key] = months.count(month)
        
        if not appointments_data:
            ax.text(0.5, 0.5, 'No appointments recorded', ha='center', va='center', 
                   transform=ax.transAxes, fontsize=14)
            ax.set_title('Total Number of Appointments per Month per Doctor')
        else:
            keys = list(appointments_data.keys())
            values = list(appointments_data.values())
            
            ax.bar(keys, values, color='coral', width=0.7)
            ax.set_ylabel('Number of Appointments')
            ax.set_title('Total Number of Appointments per Month per Doctor')
            ax.set_ylim(0, max(values + [2]))
            
            for i, v in enumerate(values):
                ax.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold')
            
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
        
        fig.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, master=self.report_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def show_illness_chart(self, dialog):
        """Illness types chart"""
        self.clear_report_frame()
        
        fig = Figure(figsize=(10, 6), dpi=100)
        ax = fig.add_subplot(111)
        
        count_illness = {}
        all_patients = self.patients + self.discharged_patients
        for patient in all_patients:
            for illness in patient.get_symptoms():
                count_illness[illness] = count_illness.get(illness, 0) + 1
        
        if not count_illness:
            ax.text(0.5, 0.5, 'No illness data recorded', ha='center', va='center', 
                   transform=ax.transAxes, fontsize=14)
            ax.set_title('Total Number of Patients based on Illness Type')
        else:
            illnesses = list(count_illness.keys())
            counts = list(count_illness.values())
            
            ax.bar(illnesses, counts, color='#2ca02c', width=0.6)
            ax.set_ylabel('Number of Patients')
            ax.set_title('Total Number of Patients based on Illness Type')
            ax.set_ylim(0, max(counts + [2]))
            
            for i, v in enumerate(counts):
                ax.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold')
            
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
        
        fig.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, master=self.report_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def show_all_charts(self, dialog):
        """Display all charts"""
        self.clear_report_frame()
        
        # Create a notebook (tabs) to show all charts
        notebook = ttk.Notebook(self.report_frame)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Tab 1: Total Doctors
        frame1 = ttk.Frame(notebook)
        notebook.add(frame1, text="Total Doctors")
        fig1 = Figure(figsize=(8, 4), dpi=80)
        ax1 = fig1.add_subplot(111)
        total_doctors = len(self.doctors)
        ax1.bar(['Total Doctors'], [total_doctors], color='steelblue', width=0.5)
        ax1.set_ylabel('Count')
        ax1.set_title('Total Number of Doctors in the System')
        ax1.text(0, total_doctors + 0.1, str(total_doctors), ha='center', va='bottom', fontweight='bold')
        fig1.tight_layout()
        canvas1 = FigureCanvasTkAgg(fig1, master=frame1)
        canvas1.draw()
        canvas1.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        frame2 = ttk.Frame(notebook)
        notebook.add(frame2, text="Patients per Doctor")
        fig2 = Figure(figsize=(8, 4), dpi=80)
        ax2 = fig2.add_subplot(111)
        doctor_names = [f"Dr. {d.full_name()}" for d in self.doctors]
        patient_counts = [len(d.get_patients()) for d in self.doctors]
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
        ax2.bar(doctor_names, patient_counts, color=colors[:len(self.doctors)], width=0.6)
        ax2.set_ylabel('Number of Patients')
        ax2.set_title('Patients per Doctor')
        for i, v in enumerate(patient_counts):
            ax2.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold')
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')
        fig2.tight_layout()
        canvas2 = FigureCanvasTkAgg(fig2, master=frame2)
        canvas2.draw()
        canvas2.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        frame3 = ttk.Frame(notebook)
        notebook.add(frame3, text="Appointments/Month")
        fig3 = Figure(figsize=(8, 4), dpi=80)
        ax3 = fig3.add_subplot(111)
        appointments_data = {}
        for doctor in self.doctors:
            appointments = doctor.get_appointments()
            if appointments:
                months = [appnmt.get_date() for appnmt in appointments]
                for month in set(months):
                    key = f"{month} - Dr. {doctor.full_name()}"
                    appointments_data[key] = months.count(month)
        
        if not appointments_data:
            ax3.text(0.5, 0.5, 'No appointments recorded', ha='center', va='center', 
                    transform=ax3.transAxes, fontsize=12)
        else:
            keys = list(appointments_data.keys())
            values = list(appointments_data.values())
            ax3.bar(keys, values, color='coral', width=0.7)
            ax3.set_ylabel('Number of Appointments')
            ax3.set_title('Appointments per Month per Doctor')
            for i, v in enumerate(values):
                ax3.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold')
            plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45, ha='right')
        fig3.tight_layout()
        canvas3 = FigureCanvasTkAgg(fig3, master=frame3)
        canvas3.draw()
        canvas3.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        frame4 = ttk.Frame(notebook)
        notebook.add(frame4, text="Illness Types")
        fig4 = Figure(figsize=(8, 4), dpi=80)
        ax4 = fig4.add_subplot(111)
        count_illness = {}
        all_patients = self.patients + self.discharged_patients
        for patient in all_patients:
            for illness in patient.get_symptoms():
                count_illness[illness] = count_illness.get(illness, 0) + 1
        
        if not count_illness:
            ax4.text(0.5, 0.5, 'No illness data recorded', ha='center', va='center', 
                    transform=ax4.transAxes, fontsize=12)
        else:
            illnesses = list(count_illness.keys())
            counts = list(count_illness.values())
            ax4.bar(illnesses, counts, color='#2ca02c', width=0.6)
            ax4.set_ylabel('Number of Patients')
            ax4.set_title('Patients by Illness Type')
            ax4.set_ylim(0, max(counts + [2]))
            for i, v in enumerate(counts):
                ax4.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold')
            plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45, ha='right')
        fig4.tight_layout()
        canvas4 = FigureCanvasTkAgg(fig4, master=frame4)
        canvas4.draw()
        canvas4.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def logout(self):
        """Logout"""
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.admin.save_patient_info(self.patients)
            self.logged_in = False
            self.show_login_window()


def main():
    root = tk.Tk()
    app = HospitalManagementGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
