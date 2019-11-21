import cozmo


def interpret(D):
    for k, v in D.items():
        for command in v:
            if command == 'SAY':
                cozmo.run_program(cozmo_program)
            if command == 'LIGHT':
                print(D)
    # print(D)


def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Hello World").wait_for_completed()


# D = {"action": "say", "text": "hello"}
# interpret(D)
