# Hospital Management System

A Python-based Hospital Management System for managing doctors, patients, and appointments with both GUI and command-line interfaces.

## Features

- Admin authentication
- Doctor management (register, view, update, delete)
- Patient management with medical records
- Appointment scheduling
- Patient discharge tracking
- Data visualization with matplotlib
- GUI and CLI interfaces

## Project Structure

```
├── Main.py              # CLI entry point
├── GUI_Main.py          # GUI entry point
├── Person.py            # Base class
├── Doctor.py            # Doctor class
├── Patient.py           # Patient class
├── Admin.py             # Admin authentication
├── Appointment.py       # Appointment class
├── patients.txt         # Data storage
```

## Installation

```bash
pip install matplotlib
```

## Usage

### GUI Interface
```bash
python GUI_Main.py
```

### CLI Interface
```bash
python Main.py
```

**Login:** username: `admin` | password: `123`

## Classes

- **Person** - Base class with name management
- **Doctor** - Extends Person, manages speciality and patients
- **Patient** - Extends Person, manages medical records and symptoms
- **Admin** - Handles authentication and operations
- **Appointment** - Manages appointment scheduling

## Default Data

**Doctors:**
- John Smith - Internal Medicine
- Jone Smith - Pediatrics
- Jone Carlos - Cardiology

**Patients:**
- Sara Smith, 20, Birmingham
- Mike Jones, 37, Liverpool
- Daivd Smith, 15, Manchester

