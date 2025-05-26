# Generates a shell script from an AST
# Core Bash generator
from . import utils


def create_val(val):
    if 0:
        pass
    else:
        utils.error(f"unknown value type '{type(val).__name__}'")


def create_block(block: list, indent=0):
    compiled = ""
    for command in block:
        compiled += ("   " * indent) + create_command(command) + "\n"

    return compiled


def create_command(command):
    compiled = ""
    if 0:
        pass
    else:
        utils.error(f"unknown command '{type(command).__name__}'")

    return compiled


def generate(program) -> str:
    return ""
    # return create_block(program)
