import gdb, os, signal

def exit_handler(event):
    """
    Print '\x1a\x19' to gdb buffer to indicate a process has terminated.
    """
    print('\x1a\x19')

def prompt_hook(prompt):
    print('\x1a\x18')
    # if prompt_hook.__first:
    #     prompt_hook.__first = False
    # else:
    #     gdb.execute('interp mi "-break-list"')
    print('\x1a\x18')

prompt_hook.__first = True

gdb.events.exited.connect(exit_handler)
gdb.prompt_hook = prompt_hook

gdb.execute('source ' + os.path.dirname(os.path.abspath(__file__)) + '/conque_gdb.gdb', False, True)
