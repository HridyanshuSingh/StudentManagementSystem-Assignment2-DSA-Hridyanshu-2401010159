from abc import ABC

class Person(ABC):
    def _init_(self, name="", email=""):
        self._name = name
        self._email = email

    def get_name(self): return self._name
    def set_name(self, name): self._name = name

    def get_email(self): return self._email
    def set_email(self, email): self._email = email

class Learner(Person):
    def _init_(self):
        super()._init_()
        self._roll_no = 0
        self._course = ""
        self._marks = 0
        self._grade = 'N'

    def add_interactive(self):
        print("\n--- Enter Student Details ---")
        self.set_name(input("Enter name: "))
        self.set_email(input("Enter email: "))
        self.set_course(input("Enter course: "))
        while True:
            try:
                roll = int(input("Enter roll number: "))
                self.set_roll_no(roll)
                break
            except ValueError:
                print("Invalid input. Enter a valid roll number.")
        while True:
            try:
                marks = int(input("Enter marks (out of 100): "))
                if 0 <= marks <= 100:
                    self.set_marks(marks)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number between 0 and 100.")
        grade_input = input("Enter grade (e.g., A, B, C): ").strip().upper()
        self.set_grade(grade_input[0] if grade_input else 'N')

    def view(self):
        print(f"Name: {self.get_name()}")
        print(f"Email: {self.get_email()}")
        print(f"Course: {self.get_course()}")
        print(f"Roll Number: {self.get_roll_no()}")
        print(f"Marks: {self.get_marks()}")
        print(f"Grade: {self.get_grade()}")

    def _str_(self):
        return (f"Learner(name='{self.get_name()}', email='{self.get_email()}', "
                f"course='{self.get_course()}', rollNo={self.get_roll_no()}, "
                f"marks={self.get_marks()}, grade='{self.get_grade()}')")

    def get_roll_no(self): return self._roll_no
    def set_roll_no(self, roll_no): self._roll_no = roll_no

    def get_course(self): return self._course
    def set_course(self, course): self._course = course

    def get_marks(self): return self._marks
    def set_marks(self, marks): self._marks = marks

    def get_grade(self): return self._grade
    def set_grade(self, grade): self._grade = grade

def main():
    students = []
    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            s = Learner()
            s.add_interactive()
            students.append(s)
            print("Student added successfully!")
        elif choice == '2':
            if not students:
                print("No students recorded yet.")
            else:
                print("\n--- List of Students ---")
                for i, st in enumerate(students, start=1):
                    print(f"Student {i}:")
                    st.view()
                    print("------------------------")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
