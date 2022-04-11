priority = 2000

requires_output = False

enabled_by_default = True


#
# def match(command):
#     return sum([ch.isupper() for ch in command.script]) > sum([ch.islower() for ch in command.script])
#
#
# def get_new_command(command):
#     return command.script.lower()


def match(command):
    if command.script_parts[0] == 'CD':
        return True


def get_new_command(command):
    return 'cd' + ''.join(command.script[2:])
