

def match(command):
    # return sum([ch.isupper() for ch in command.script]) > sum([ch.islower() for ch in command.script])
    if command.script.isupper():
        return True


def get_new_command(command):
    return command.script.lower()


priority = 1500

requires_output = False

enabled_by_default = True
