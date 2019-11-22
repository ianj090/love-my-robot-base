import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time

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

    def DRIVE(self, num1, num2):
        def cozmo_program(robot: cozmo.robot.Robot):
            # Drive forwards for 150 millimeters at 50 millimeters-per-second.
            robot.drive_straight(distance_mm(num1), speed_mmps(num2)).wait_for_completed()
        cozmo.run_program(cozmo_program)
    
    def TURN(self, var1):
        def cozmo_program(robot: cozmo.robot.Robot):
            # Drive forwards for 150 millimeters at 50 millimeters-per-second.
            robot.turn_in_place(degrees(var1)).wait_for_completed()
        cozmo.run_program(cozmo_program)
    
    def LIFT(self, number1):
        def cozmo_program(robot: cozmo.robot.Robot):
            # Drive forwards for 150 millimeters at 50 millimeters-per-second.
            robot.set_lift_height(number1).wait_for_completed()
        cozmo.run_program(cozmo_program)

    def LIGHT(self, color):
        def cozmo_program(robot: cozmo.robot.Robot):
            cube1 = robot.world.get_light_cube(1) #LightCube1Id  # looks like a paperclip
            cube2 = robot.world.get_light_cube(2)  # looks like a lamp / heart
            cube3 = robot.world.get_light_cube(3)  # looks like the letters 'ab' over 'T'

            if cube1 is not None:
                cube1.set_lights(color)
            else:
                cozmo.logger.warning("Cozmo is not connected to a LightCube1Id cube - check the battery.")

            if cube2 is not None:
                cube2.set_lights(color)
            else:
                cozmo.logger.warning("Cozmo is not connected to a LightCube2Id cube - check the battery.")

            if cube3 is not None:
                cube3.set_lights(color)
            else:
                cozmo.logger.warning("Cozmo is not connected to a LightCube3Id cube - check the battery.")

            # Keep the lights on for 10 seconds until the program exits
            time.sleep(10)


        cozmo.run_program(cozmo_program)


    def WHEELIE(self, number):
        def cozmo_program(robot: cozmo.robot.Robot):
            cube1 = robot.world.get_light_cube(number)  # looks like a paperclip
            robot.pop_a_wheelie(cube1).wait_for_completed()
        cozmo.run_program(cozmo_program)

# yeah


def interpret(D):
    L = []  # para las variables
    try:
        inner_list = D["lmr"]
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
        elif item == '10':
            for b in range(0, 10):
                I = run_cozmo(b)
                I.SAY()

        elif item == '15':
            for c in range(0, 8):
                I = run_cozmo(c)
                I.SAY()

    # YES
        elif item == 'YES':
            I = run_cozmo(item)
            I.SAY()

    # DRIVE
        elif item == 'Forward':
            first = 150
            second = 50
            I = run_cozmo(None)
            I.DRIVE(first, second)
        elif item == 'Forward a little':
            first = 75
            second = 50
            I = run_cozmo(None)
            I.DRIVE(first, second)
        elif item == 'Backward':
            first = -150
            second = 50
            I = run_cozmo(None)
            I.DRIVE(first, second)
        elif item == 'Backward a little':
            first = -75
            second = 50
            I = run_cozmo(None)
            I.DRIVE(first, second)

    # TURN
        elif item == 'Right':
            degree = 90
            I = run_cozmo(None)
            I.TURN(degree)
        elif item == 'Left':
            degree = -90
            I = run_cozmo(None)
            I.TURN(degree)
        elif item == 'Turn back':
            degree = -180
            I = run_cozmo(None)
            I.TURN(degree)

    # LIFT
        elif item == 'LIFT 1':
            height = 1.0
            I = run_cozmo(None)
            I.LIFT(height)
        elif item == 'LIFT 0.8':
            height = 0.8
            I = run_cozmo(None)
            I.LIFT(height)
        elif item == 'LIFT 0.5':
            height = 0.5
            I = run_cozmo(None)
            I.LIFT(height)

    # LIGHT
        elif item == 'Green':
            cubes_colors = cozmo.lights.green_light
            I = run_cozmo()
            I.LIFT(cubes_colors)
        elif item == 'Red':
            cubes_colors = cozmo.lights.red_light
            I = run_cozmo()
            I.LIFT(cubes_colors)
        elif item == 'Blue':
            cubes_colors = cozmo.lights.blue_light
            I = run_cozmo()
            I.LIFT(cubes_colors)
    
    # WHEELIE
        elif item == 'WHEELIE 1':
            cube_number = 1
            I = run_cozmo()
            I.WHEELIE(cube_number)
        elif item == 'WHEELIE 2':
            cube_number = 2
            I = run_cozmo()
            I.WHEELIE(cube_number)
        elif item == 'WHEELIE 3':
            cube_number = 3
            I = run_cozmo()
            I.WHEELIE(cube_number)
    
    # CUBE
        elif item == 'Circles':
            cube_number = 1
            I = run_cozmo()
            I.CUBE(cube_number)


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
