from thefuck.utils import get_all_executables, get_close_matches, get_close_matches_icase, \
    get_valid_history_without_current, get_closest, which
from thefuck.specific.sudo import sudo_support


@sudo_support
def match(command):
    return (not which(command.script_parts[0])
            and ('not found' in command.output
                 or 'is not recognized as' in command.output)
            and bool(get_close_matches_icase(command.script_parts[0],
                                             get_all_executables())))


def _get_used_executables(command):
    for script in get_valid_history_without_current(command):
        yield script.split(' ')[0]


@sudo_support
def get_new_command(command):
    old_command = command.script_parts[0]

    # One from history:
    already_used = get_closest(
        old_command, _get_used_executables(command),
        fallback_to_first=False)
    if already_used:
        new_cmds = [already_used]
    else:
        new_cmds = []

    # Other from all executables:
    new_cmds += [cmd for cmd in get_close_matches(old_command,
                                                  get_all_executables())
                 if cmd not in new_cmds]

    return [' '.join([new_command] + command.script_parts[1:])
            for new_command in new_cmds]


priority = 3000
