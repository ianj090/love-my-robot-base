import cozmo


def interpret(D):
    for k, v in D.items():
        if v[0] == 'SAY':
            print(D)
        if v[1] == 'LIGHT':
            print(D)
    # print(D)


# D = {"action": "say", "text": "hello"}
# interpret(D)
