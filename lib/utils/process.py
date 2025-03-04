import subprocess

def run_program(program_path, arg_1='', arg_2=''):
    process = subprocess.Popen(
        (program_path, arg_1, arg_2),
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE
        # startupinfo=startupinfo
    )
    return process