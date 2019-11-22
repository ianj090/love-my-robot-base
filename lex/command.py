import cozmo

D = {"commands": ["I love you",
                  "Hello World",
                  "Sorry",
                  "How are you"
                  ]}


# variable = ""

# def run_cozmo(variable):
#     def cozmo_say_hello(): # robot: cozmo.robot.Robot
#         variable =  variable ** 2
#         print(variable)
#         # robot.say_text(variable).wait_for_completed()
#     # cozmo.run_program(cozmo_program)
#     cozmo_say_hello()

# run_cozmo(48)



class run_cozmo():
    def __init__(self, command):
        self.command = command
    
    def SAY(self):
        def cozmo_program(robot: cozmo.robot.Robot):
            robot.say_text(str(self.command)).wait_for_completed() 
        cozmo.run_program(cozmo_program)

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
        
    def COUNT(self):
        '''
        5
        10
        50
        100
        '''
        def cozmo_program(robot: cozmo.robot.Robot):
            robot.say_text(str(self.command)).wait_for_completed() 
        cozmo.run_program(cozmo_program)
        
    def DRIVE(self):
        '''
        forward (MOVE 150 50)
        forward a little (MOVE 75 50)
        backward (MOVE -150,50)
        backward a little (MOVE -75 50)
        '''
        def cozmo_program(robot: cozmo.robot.Robot):
            robot.say_text(str(self.command)).wait_for_completed() 
        cozmo.run_program(cozmo_program)
        
    def TURN(self):
        '''
        right (90 100)
        left (-90 100)
        turn back (-180 100)
        '''
        def cozmo_program(robot: cozmo.robot.Robot):
            robot.say_text(str(self.command)).wait_for_completed() 
        cozmo.run_program(cozmo_program)
        
    def LIFT(self):
        '''
        1
        0.8
        0.5
        '''
        def cozmo_program(robot: cozmo.robot.Robot):
            robot.say_text(str(self.command)).wait_for_completed() 
        cozmo.run_program(cozmo_program)
        
    def LIGHT(self):
        '''
        Green
        red
        blue
        '''
        def cozmo_program(robot: cozmo.robot.Robot):
            robot.say_text(str(self.command)).wait_for_completed() 
        cozmo.run_program(cozmo_program)
        
    def WHEELIE(self):
        '''
        1
        2
        3
        '''
        def cozmo_program(robot: cozmo.robot.Robot):
            robot.say_text(str(self.command)).wait_for_completed() 
        cozmo.run_program(cozmo_program)
        
    def CUBE(self):
        '''
        circles
        diamonds
        triangles
        '''
        def cozmo_program(robot: cozmo.robot.Robot):
            robot.say_text(str(self.command)).wait_for_completed() 
        cozmo.run_program(cozmo_program)
        
    def PICKUP(self):
        '''
        1
        2
        3
        '''
        def cozmo_program(robot: cozmo.robot.Robot):
            robot.say_text(str(self.command)).wait_for_completed() 
        cozmo.run_program(cozmo_program)
        
    def DROP(self):
        def cozmo_program(robot: cozmo.robot.Robot):
            robot.say_text(str(self.command)).wait_for_completed() 
        cozmo.run_program(cozmo_program)


def interpret(D):
    try:
        inner_list = D["commands"]
    except:
        inner_list = None

    for item in 








        
    # SAY
        # if item == 'Hello World':
        #     I = run_cozmo(item)
        #     I.SAY()

        # elif item == 'I love you':
        #     I = run_cozmo(item)
        #     I.SAY()

        # elif item == 'How are you?':
        #     I = run_cozmo(item)
        #     I.SAY()

        # elif item == 'Sorry':
        #     I = run_cozmo(item)
        #     I.SAY()
    
        # elif item == 'You are funny!':
        #     I = run_cozmo(item)
        #     I.SAY()

        # elif item == 'Wanna be friends?':
        #     I = run_cozmo(item)
        #     I.SAY()

        # elif item == 'No':
        #     I = run_cozmo(item)
        #     I.SAY()

        # elif item == 'What’s your name?':
        #     I = run_cozmo(item)
        #     I.SAY()

        # elif item == 'AHHH! Humans!':
        #     I = run_cozmo(item)
        #     I.SAY()

        # elif item == 'You’ll never catch me!':
        #     I = run_cozmo(item)
        #     I.SAY()

        # elif item == 'Thank You':
        #     I = run_cozmo(item)
        #     I.SAY()

        # elif item == 'You are ugly':
        #     I = run_cozmo(item)
        #     I.SAY()

        # elif item == 'You are Beautiful':
        #     I = run_cozmo(item)
        #     I.SAY()

        # elif item == 'Goodbye':
        #     I = run_cozmo(item)
        #     I.SAY()

        # elif item == 'Eureka':
        #     I = run_cozmo(item)
        #     I.SAY()


    # MATH
        # elif item == '10+10'
        #     I = run_cozmo()
        #     I.MATH()
            
        # elif item == '100/5'
        #     I = run_cozmo()
        #     I.MATH()
            
        # elif item == '(5/2) * 4'
        #     I = run_cozmo()
        #     I.MATH()
        
        # elif item == '23924/12340*139843+2334-234'
        #     I = run_cozmo()
        #     I.MATH()
        
        # elif item == '(2+45-90)20'
        #     I = run_cozmo()
        #     I.MATH()
        
        # elif item == '40*34/67'
        #     I = run_cozmo()
        #     I.MATH()
        
        # elif item == '200-100'
        #     I = run_cozmo()
        #     I.MATH()
        
        # elif item == '10000000-99999999'
        #     I = run_cozmo()
        #     I.MATH()

    
    # COUNT
        # elif item == '5':
        #     I = run_cozmo(item)
        #     I.COUNT()
		# elif item == '10':
        #     I = run_cozmo(item)
        #     I.COUNT()
		# elif item == '50':
        #     I = run_cozmo(item)
        #     I.COUNT()
		# elif item == '100':
        #     I = run_cozmo(item)
        #     I.COUNT()
    
    # YES
        # elif item == 'YES':
        #     I = run_cozmo(item)
        #     I.YES()

    # DRIVE
        # elif item == 'forward':
        #     first = 150
        #     second = 50
        #     I = run_cozmo(first, second)
        #     I.YES()
        # elif item == 'forward a little':
        #     first = 75
        #     second = 50
        #     I = run_cozmo(first, second)
        #     I.YES()
        # elif item == 'backward':
        #     first = -150
        #     second = 50
        #     I = run_cozmo(first, second)
        #     I.YES()
        # elif item == 'backward a little':
        #     first = -75
        #     second = 50
        #     I = run_cozmo(first, second)
        #     I.YES()
    

    
if __name__ == "__main__":
    interpret(D)

# MATH 
#   "10+10"
#   "100/5"
#   "(5/2) * 4"
#   "23924/12340*139843+2334-234"
#   "(2+45-90)20"
#   "40*34/67"
#   "200-100"
#   "10000000-99999999"
# COUNT 
# 5
# 10
# 50
# 100
# YES 
# >>>>>(MOVEMENT)
# DRIVE
#   forward (MOVE 150 50)
#   forward a little (MOVE 75 50)
#   backward (MOVE -150,50)
#   backward a little (MOVE -75 50)
# TURN
# 	right (90 100)
# 	left (-90 100)
# 	turn back (-180 100)
# LIFT
# 	1
# 	0.8
# 	0.5
# >>>>>(ANIMATIONS)
# LIGHT
# 	Green
# 	red
# 	blue
# WHEELIE
# 1
# 2
# 3
# CUBE
# circles
# diamonds
# triangles
# PICKUP
# 1
# 2
# 3
# DROP

        



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


