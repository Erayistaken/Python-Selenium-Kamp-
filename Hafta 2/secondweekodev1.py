# listeye öğrenci ekleme

students = []
print(students)
studentName = input("Öğrenci ismi giriniz")
studentLastname = input("Öğrenci soyismi giriniz")
students.append(studentName+" "+studentLastname)
print(students)

# Öğrenci silme
studentNameLastname = input(
    "Silmek istediğiniz öğrencinin ismini ve soyismini giriniz. : ")

for students in students:
    if students == studentNameLastname:
        students.remove(students)
        print(f"{studentNameLastname}listeden silinmiştir.")
    else:
        print(f"{studentNameLastname}listede bulunamamıştır.")

        # Listeye birden fazla öğrenci eklemeyi mümkün kılan

        number = int(input("Kaç öğrenci eklemek istiyorsunuz?"))
        i = 0
        while (i < number):
            newStudent = input("İsim ve soyisim: ")
            students.append(newStudent)
            i += 1
            print(students)

        # Listedeki tüm öğrencileri tek tek ekrana yazdıran
        for students in students:
            print(students)

            # Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan

            studentNo = input(
                "Numarasını öğrenmek istediğiniz öğrencinin isim ve soyismini giriniz: ")

            for studentNumber in students:
                if studentNumber == studentNo:
                    studentNo = students.index(studentNumber) + 1
                    print("Öğrenci numarası:", studentNo)

                else:
                    print(f"{studentNumber} listede bulunamamıştır.")

                    # listeden birden fazla öğrenci silmeyi mümkün kılan

                    studentDelete = int(
                        input("Silmek istedğiniz öğrencinin numarasını giriniz: "))

                    i = 0
                    while (i < studentDelete):
                        deletedStudent = input("İsim Soyisim:")
                        students.remove(deletedStudent)

                        print(f"Güncel Liste:  {students} ")
