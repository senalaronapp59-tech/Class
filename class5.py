class Alumno:
    def __init__(self,name,age,dob,id_number):
        self.Alumno_name = name
        self.Alumno_age = age
        self.Alumno_dob = dob
        self.Alumno_id = id_number   
    def add_alumno(self):
        print("Nombre:"+ self.Alumno_name)
        print("Edad:"+ self.Alumno_age)
        print("Nacimiento:"+ self.Alumno_dob)
        print("Id alumno:"+ self.Alumno_id)
        print("Alumno agregado")
        
Alumno1 = Alumno("Jasiel","13","2 de agosto de 2012","001")
Alumno1.add_alumno()
Alumno2 = Alumno("Mateo","14","3 de diciembre de 2012","002")
Alumno2.add_alumno()
        