import cozmo

D = {"commands": ["I love you",
                  "Hello World",
                  "Sorry",
                  "How are you"
                  ]}


class run_cozmo():
    def __init__(self, command,):
        self.command = command

    def SAY(self):
        def cozmo_program(robot: cozmo.robot.Robot):
            robot.say_text(str(self.command)).wait_for_completed()
        cozmo.run_program(cozmo_program)
        code = '''
        def SAY(s):
            def cozmo_program(robot: cozmo.robot.Robot):
                robot.say_text(str({})).wait_for_completed() 
            cozmo.run_program(cozmo_program)
        '''.format(self.command)
        return code

    def MATH(self):
        '''
        10+10
        100/5
        (5/2) * 4
        239/140*139843+2334-234
        (2+45-90)20
        40*34/67
        200-100
        10000000-99999999
        '''
        def cozmo_program(robot: cozmo.robot.Robot):
            robot.say_text(str(self.command)).wait_for_completed()
        cozmo.run_program(cozmo_program)

    def movement(self, num1, num2):
        def cozmo_program(robot: cozmo.robot.Robot):
            # Drive forwards for 150 millimeters at 50 millimeters-per-second.
            robot.drive_straight(distance_mm(
                num1), speed_mmps(num2)).wait_for_completed()
        cozmo.run_program(cozmo_program)

# yeah


def interpret(D):
    L = []  # para las variables
    try:
        inner_list = D["commands"]
    except:
        inner_list = None

    for item in inner_list:
        # SAY
        if item == 'Hello World':
            I = run_cozmo(item)
            temp = I.SAY()
            L.append(temp)

        elif item == 'I love you':
            I = run_cozmo(item)
            temp = I.SAY()
            L.append(temp)

        elif item == 'How are you?':
            I = run_cozmo(item)
            temp = I.SAY()
            L.append(temp)

        elif item == 'Sorry':
            I = run_cozmo(item)
            temp = I.SAY()
            L.append(temp)

        elif item == 'You are funny!':
            I = run_cozmo(item)
            temp = I.SAY()
            L.append(temp)

        elif item == 'Wanna be friends?':
            I = run_cozmo(item)
            temp = I.SAY()
            L.append(temp)

        elif item == 'No':
            I = run_cozmo(item)
            temp = I.SAY()
            L.append(temp)

        elif item == 'What’s your name?':
            I = run_cozmo(item)
            temp = I.SAY()
            L.append(temp)

        elif item == 'AHHH! Humans!':
            I = run_cozmo(item)
            temp = I.SAY()
            L.append(temp)

        elif item == 'You’ll never catch me!':
            I = run_cozmo(item)
            temp = I.SAY()
            L.append(temp)

        elif item == 'Thank You':
            I = run_cozmo(item)
            temp = I.SAY()
            L.append(temp)

        elif item == 'You are ugly':
            I = run_cozmo(item)
            temp = I.SAY()
            L.append(temp)

        elif item == 'You are Beautiful':
            I = run_cozmo(item)
            temp = I.SAY()
            L.append(temp)

        elif item == 'Goodbye':
            I = run_cozmo(item)
            temp = I.SAY()
            L.append(temp)

        elif item == 'Eureka':
            I = run_cozmo(item)
            temp = I.SAY()
            L.append(temp)

    # MATH
        elif item == '10+10':
            I = run_cozmo(20)
            I.MATH()

        elif item == '100/5':
            I = run_cozmo(20)
            I.MATH()

        elif item == '(5/2) * 4':
            I = run_cozmo(10)
            I.MATH()

        elif item == '239/140*139+2334-234':
            I = run_cozmo(0.01)
            I.MATH()

        elif item == '(2+45-90)20':
            I = run_cozmo(-860)
            I.MATH()

        elif item == '40*34/67':
            I = run_cozmo(20.29)
            I.MATH()

        elif item == '200-100':
            I = run_cozmo(100)
            I.MATH()

        elif item == '10000000-99999999':
            I = run_cozmo(1)
            I.MATH()

    # COUNT
        elif item == '5':
            for a in range(0, 5):
                I = run_cozmo(a)
                I.SAY()
        elif item == '7':
            for b in range(0, 7):
                I = run_cozmo(b)
                I.SAY()

        elif item == '8':
            for c in range(0, 8):
                I = run_cozmo(c)
                I.SAY()

        elif item == '10':
            for d in range(0, 10):
                I = run_cozmo(d)
                I.SAY()

    # YES
        elif item == 'YES':
            I = run_cozmo(item)
            I.SAY()

    # DRIVE
        elif item == 'forward':
            first = 150
            second = 50
            I = run_cozmo(None)
            I.movement(first, second)
        elif item == 'forward a little':
            first = 75
            second = 50
            I = run_cozmo(None)
            I.movement(first, second)
        elif item == 'backward':
            first = -150
            second = 50
            I = run_cozmo(None)
            I.movement(first, second)
        elif item == 'backward a little':
            first = -75
            second = 50
            I = run_cozmo(None)
            I.movement(first, second)


if __name__ == "__main__":
    interpret(D)


# import cozmo

# D =  {"commands": ["Hello World", "I love you", "Sorry"]}

# variable = ""

# def interpret(D):
#     try:
#         inner_list = D["commands"]
#     except:
#         inner_list = None

#     global variable
#     for item in inner_list:
#         # SAY
#         variable = item
#         print(variable)
#         cozmo.run_program(cozmo_program)


# def cozmo_program(robot: cozmo.robot.Robot):
#     robot.say_text(variable).wait_for_completed()

# interpret(D)
