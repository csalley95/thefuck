priority = 2000

requires_output = False

enabled_by_default = True


def match(command):
    return sum([ch.isupper() for ch in command.script]) > sum([ch.islower() for ch in command.script])


def get_new_command(command):
    return command.script.lower()
