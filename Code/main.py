from Function import Calculator, Calculus, Statistic, Matrix, Base_number 
from text import * 
cal = Calculator()
stat = Statistic()
matrix = Matrix()
base = Base_number()
calculus = Calculus()


expression = ""

# Dictionary สำหรับเรียกใช้ฟังก์ชั่น แต่ละแบบ

# สำหรับสถิติ
statistic_call = {
    1: stat.summation,
    2: stat.findAverage,
    3: stat.findMedian,
    4: stat.findRange,
    5: stat.findVariance,
    6: stat.findVariance,
    7: stat.findCnr,
    8: stat.findPnr,
    9: stat.findPnorm
}

# สำหรับ calculus
calculus_call = {
    1: calculus.limit,
    2: calculus.differential,
    3: calculus.integral,
    4: calculus.areaIntegral
}

# สำหรับเลขฐาน
base_number_call = {
    1: base.toTwo,
    2: base.toOct,
    3: base.toTen,
    4: base.toHex
}

# สำหรับ Matrix
matrix_call = {
    1: matrix.plusMatrix,
    2: matrix.multiply_matrix,
    3: matrix.scale_matrix,
    4: matrix.inverse_matrix
}

while 1:

    # print menu เฉยๆมีไร
    print(f"""

{"="*50}Menu{"="*50}
1.) Calculator
2.) Statistic 
3.) Calculus
4.) Matrix 
5.) Convert to base-number
6.) Exit """)

    # รับ menu จาก user
    try:
        menu = int(input("Which menu do you like to choose : "))
    except ValueError:
        print(
            "\n[Error] Something went wrong please make sure what you've entered was correct")
        continue
    print()

    # This is for calculator functions
    if menu == 1:

        # รับค่าจาก user
        try:
            expression = input(
                "Enter you expression or enter '0' to exit this menu : ").strip()
        except ValueError:
            print(
                "\n[Error] Something went wrong please make sure what you've entered was correct")
            continue

        # ถ้าเป็น 0 คือออกจากเมนูนี้
        if expression == '0':
            continue

        print(f"\n{'='*35}")
        # ถ้าไม่ใช่ 0 จะคำนวณสิ่งที่ user ป้อนเข้ามา และ print ออกมา
        try :
            try:
               print(f"Result :", cal.calculate(expression))
            except NameError :
               print(
                "\n[Error] Something went wrong please make sure what you've entered was correct")
               continue
        except SyntaxError :
            print(
                "\n[Error] Something went wrong please make sure what you've entered was correct")
            continue
        print(f"{'='*35}")

    # This is for statistis functions
    elif menu == 2:

        print(statistic_text)
        # รับ menu ของสถิติ ซึ่งมีถึง 10 เมนู!
        try:
            call = int(input("Which menu do you like to choose : ").strip())
        except ValueError:
            print(
                "\n[Error] Something went wrong please make sure what you've entered was correct")
            continue
        # ถ้าเท่ากับ 0 คือออกจากเมนูนี้
        if call == 0:
            continue

        # ป้อนเมนูเป็นเลขอะไร จะไปเรียกใช้เมนูจาก Dictionary statistic_call ตามเลขที่ป้อน
        try:
            print(f"\n{'='*35}")
            if call in [1, 2, 3, 4]:
                print("Result :", statistic_call[call](
                    input("Enter list of number(using spacebar) : ").strip()))

            elif call == 5:
                print("Result :", statistic_call[call](
                    input("Enter list of number(using spacebar) : ").strip())[1]
                )

            elif call == 6:
                print("Result :", statistic_call[call](
                    input("Enter list of number(using spacebar) : ").strip())[0]
                )

            elif call in [7, 8]:
                print("Result :", statistic_call[call](
                    int(input("Enter n : ").strip()), int(
                        input("Enter r : ").strip())
                ))

            elif call == 9:
                print(f"Result : ", statistic_call[call](
                    float(input("Enter x : ").strip()), float(
                        input("Enter μ : ").strip()),
                    float(input("Enter \u03c3 : ").strip()), int(
                        input("Enter n : ").strip())
                ))
            print(f"{'='*35}")
        except ValueError:
            print(
                "\n[Error] Something went wrong please make sure what you've entered was correct")
            continue

    # This is for calculus functions
    elif menu == 3:

        print(calculus_text)
        # รับเมนู
        try:
            call_cal = int(
                input("Which menu do you like to choose : ").strip())
        except ValueError:
            print(
                "\n[Error] Something went wrong please make sure what you've entered was correct")
            continue
        # เป็น 0 ก็ออกจากเมนู
        if call_cal == 0:
            continue

        # เลือกเลขไหน ก็จะเรียกใช้ฟังก์ชั่นตามชื่อที่เห็นเลย ชื่อฟังก์ชั่นสือความหมายแล้ว
        print(f"\n{'='*35}")
        try:
            if call_cal == 1:
                f = input("Enter f(x) : ").strip()
                x = int(input("Enter limit to : ").strip())
                print("Result :", calculus.limit(f, x))

            elif call_cal == 2:
                f = input("Enter f(x) : ")
                result = calculus.differential(f)

                print("Result :", result)
                while 1:
                    more = input(
                        "Do you want to diff more? [yes,no] : ").strip()
                    if more == 'yes':
                        result = calculus.differential(result)
                        print("Result :", result)
                    elif more == 'no':
                        break

            elif call_cal == 3:
                print("Result :", calculus.integral(
                    input("Enter f(x) : ").strip()))

            elif call_cal == 4:
                print("Result :", calculus.areaIntegral(
                    input("Enter f(x) : ").strip(), int(
                        input("Enter start : ").strip()),
                    int(input("Enter stop : ").strip())
                ))
        except ValueError:
            print(
                "\n[Error] Something went wrong please make sure what you've entered was correct")
            continue
        print(f"{'='*35}")

    # This is for Matix functions
    elif menu == 4:

        print(matrix_text)
        # รับเมนู
        try:
            call_matrix = int(
                input("Which menu do you like to choose : ").strip())
        except ValueError:
            print(
                "\n[Error] Something went wrong please make sure what you've entered was correct")
            continue

        # เป็น 0 ก็ออกจากเมนู
        if call_matrix == 0:
            continue
        print(f"{'='*35}")

        # ป้อนเลข 1 จะเรียกใช้ฟังก์ชั่น plus_matrix
        try:
            try:
                if call_matrix == 1:
                    print(matrix.plusMatrix(
                        input("Enter list of number(Using spacebar) : ").strip(),
                        input("Enter list of number(Using spacebar) : ").strip()
                    ))

        # เลขอื่นๆ จะเรียกใช้ฟังก์ชั่นตามเลขที่ป้อน อ้างอิงจาก dict matrix_call
                else:
                    matrix_call[call_matrix]()
                    print(f"{'='*35}")
            except KeyError:
                print(
                    "\n[Error] Something went wrong please make sure what you've entered was correct")
                continue
        except ValueError:
            print(
                "\n[Error] Something went wrong please make sure what you've entered was correct")
            continue

    # This is for base-number functions
    elif menu == 5:

        print(base_text)
        # รับเมนู
        try:
            call_base = int(
                input("Which menu do you like to choose : ").strip())
        # เป็น 0 ออกจากเมนู
            if call_base == 0:
                continue

            print(f"\n{'='*35}")
            # เรียกใช้ฟังก์ชั่นตามเลขที่ป้อน อ้างอิงจาก dict base_number_call
            try:
                print("Result : ", base_number_call[call_base](
                    int(input("Enter number : ").strip())))
                print(f"{'='*35}")
            except KeyError:
                print(
                    "\n[Error] Something went wrong please make sure what you've entered was correct")
                continue

        except ValueError:
            print(
                "\n[Error] Something went wrong please make sure what you've entered was correct")
            continue

    # ออกจากโปรแกรม
    elif menu == 6:
        break
