priority = 1200

requires_output = False

enabled_by_default = True


def match(command):
    if command.script_parts[0].isupper():
        return True


def get_new_command(command):
    return command.output.lower()
