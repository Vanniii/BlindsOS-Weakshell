import os
import math as m
from sys import exit
from socket import gethostname, gethostbyname
from platform import system, release, version, machine, processor, architecture
from datetime import date, datetime
from simple_colors import red, yellow, green, blue
from pythonping import ping
from re import findall
from uuid import getnode
from psutil import virtual_memory
from random import randint

# time conversions
# other conversions l8r

print('BLINDS OS WeakShell v1.0')
print("Copyright (C) Vanity's Non Existent Corp. No Rights Reserved.")
print()
print('Use the latest version of WeaknessShell for the latest features!')
print()

while True:
    currentDir = os.getcwd()
    cmd = input(f'WS {currentDir}> ').strip()

    if cmd == "help":
        print()
        print(red('== FILES AND DIRS ==', 'bold'))
        print("cd - change directory")
        print("cd/ - root directory")
        print("dir - view directory contents")
        print("mkdir - create a new directory")
        print("ren - rename file or directory")
        print("rm - delete directory")
        print('mk - creates a new file')
        print("read - view file contents")
        print("write - writes to a file")
        print("del - delete file")
        print()
        print(yellow('== SYSTEM ==', 'bold'))
        print("hostname - get hostname of PC")
        print("shutdown - shutdown PC")
        print("restart - restart PC")
        print("date - view date")
        print("time - view time")
        print("details - view details of the system")
        print()
        print(green('== NETWORK ==', 'bold'))
        print("ip -  get ip of a hostname. defaults to PC's hostname.")
        print("ping - pings an ip")
        print()
        print(blue('== OTHER ==', 'bold'))
        print('weakshell - information about weakshell')
        print('echo - echoes back a statement, or writes it to a file.')
        print('calc - help on calculation')
        print('numguess - help on number guessing game')
        print()
        print("Using some command names on their own will provide syntax.")
        print()

    elif cmd == 'exit':
        exit()

    elif cmd == 'cd':
        print('cd [directory_name]')
        print()

    elif cmd.startswith('cd '):
        directory = cmd[3:].strip()
        try:
            os.chdir(directory)
        except FileNotFoundError:
            print(red(f'Directory "{directory}" does not exist'))
            print()
        except OSError as a:
            print(red(f'The Humanity! An OSError occurred: {a}.'))
            print()

    elif cmd == 'cd/':
        drive = currentDir.split(':')[0] + '://'
        os.chdir(drive)

    elif cmd == 'dir':
        print()
        contents = os.listdir(currentDir)
        for item in contents:
            print(item)
        print()

    elif cmd == 'mkdir':
        print('mkdir [directory_name]')
        print()

    elif cmd.startswith('mkdir '):
        directory = cmd[6:].strip()
        try:
            os.mkdir(directory)
            print(red(f'Created directory "{directory}".'))
        except FileExistsError:
            print(red(f'Directory "{directory}" already exists.'))
        except PermissionError:
            print(red('The program does not have permission to create a directory in this location.'))
        except OSError as a:
            print(red(f'The Humanity! An OSError occurred: {a}.'))
        print()

    elif cmd == 'ren':
        print('ren [old_directory_name], [new_directory_name]')
        print()

    elif cmd.startswith('ren '):
        dirs = cmd[4:].split(',')
        try:
            oldDir = dirs[0].strip()
            newDir = dirs[1].strip()
            try:
                os.rename(oldDir, newDir)
                print(f'Renamed directory "{oldDir}" to "{newDir}".')
            except FileNotFoundError:
                print(red(f'Directory "{oldDir}" does not exist.'))
            except FileExistsError:
                print(red(f'Directory "{newDir}" already exists.'))
            except PermissionError:
                print(red('The program does not have permission to create a directory in this location.'))
            except OSError as a:
                print(red(f'The Humanity! An OSError occurred: {a}.'))
        except IndexError:
            print(red("Invalid syntax. Type 'ren' for more information on syntax."))
        print()

    elif cmd.strip() == 'rd':
        print('rd [dir_name]')
        print()

    elif cmd.startswith('rm '):
        directory = cmd[3:].strip()
        try:
            os.rmdir(directory)
            print(red(f'Removed directory "{directory}".'))
        except FileNotFoundError:
            print(red(f'Directory "{directory}" does not exist.'))
        except PermissionError:
            print(red('The program does not have permission to delete this directory.'))
        except OSError as a:
            print(red(f'The Humanity! An OSError occurred: {a}.'))
        print()

    elif cmd.strip() == 'mk':
        print('mk [directory_name]')
        print()

    elif cmd.startswith('mk '):
        filename = cmd[3:].strip()
        filepath = (os.path.join(currentDir, filename)).replace('\\', '/')
        try:
            f = __builtins__.open(filepath, 'x')
            print(f'Created file "{filename}".')
            f.close()
        except FileExistsError:
            print(red(f'File "{filename}" already exists.'))
        except PermissionError:
            print(red('The program does not have permission to create a file in this location.'))
        except OSError as a:
            print(red(f'The Humanity! An OSError occurred: {a}.'))
        print()

    elif cmd.strip() == 'read':
        print('read [filename]')
        print()

    elif cmd.startswith('read '):
        filename = cmd[5:].strip()
        filepath = (os.path.join(currentDir, filename)).replace('\\', '/')
        try:
            f = open(filepath, 'r')
            print()
            print(f.read())
            print()
            f.close()
        except FileNotFoundError:
            print(red(f'File "{filename}" does not exist.'))
        except PermissionError:
            print(red('The program does not have permission to read this file.'))
        except OSError as a:
            print(red(f'The Humanity! An OSError occurred: {a}.'))
        print()

    elif cmd == 'write':
        print('write [filename], [contents], [mode]')
        print("Modes: 'a' - append, 'o' - overwrite")
        print()

    elif cmd.startswith('write '):
        inp = cmd[6:].split(',')
        print(inp)
        try:
            filename = inp[0].strip()
            mode = inp[2].strip()
            filepath = (os.path.join(currentDir, filename)).replace('\\', '/')
            try:
                if mode == 'a':
                    conts = inp[1]
                    f = open(filepath, 'a')
                    f.write(conts)
                    print(f'Appended to file "{filename}".')
                elif mode == 'o':
                    conts = inp[1].strip()
                    f = open(filepath, 'w')
                    f.write(conts)
                    print(f'Wrote to file "{filename}".')
            except FileNotFoundError:
                print(red(f'File "{filename}" does not exist.'))
            except PermissionError:
                print(red('The program does not have permission to write this file.'))
            except OSError as a:
                print(red(f'The Humanity! An OSError occurred: {a}.'))
        except IndexError:
            print(red("Invalid syntax. Type 'write' for more information on syntax."))
        print()

    elif cmd == 'delete':
        print('delete [filename]')
        print()

    elif cmd.startswith('del '):
        filename = cmd[4:].strip()
        try:
            os.remove(filename)
            print(red(f'Deleted file "{filename}".'))
        except FileNotFoundError:
            print(red(f'File "{filename}" does not exist.'))
        except PermissionError:
            print(red('The program does not have permission to delete this file.'))
        except OSError as a:
            print(red(f'The Humanity! An OSError occurred: {a}.'))
        print()

    elif cmd == 'hostname':
        print(gethostname())
        print()

    elif cmd == 'shutdown':
        os.system('shutdown /s /t 0')
    elif cmd == 'restart':
        os.system('shutdown /r /t 0')

    elif cmd == 'date':
        print(date.today())
        print()

    elif cmd == 'time':
        now = datetime.now()
        print(now.strftime('%H:%M:%S'))
        print()

    elif cmd == 'details':
        print()
        print('Platform:', system())
        print('Release:', release())
        print('Version:', version())
        print('Machine:', machine())
        print('Hostname:', gethostname())
        print('IP Address:', gethostbyname(gethostname()))
        print('Mac Address:', ':'.join(findall('..', '%012x' % getnode())))
        print('Processor:', processor())
        print('Architecture:', architecture())
        print('RAM:', str(round(virtual_memory().total / (1024.0 **3))) + " GB")
        print()

    elif cmd == 'ip':
        print(gethostbyname(gethostname()))
        print()

    elif cmd == 'ping':
        print('ping [address]')
        print()

    elif cmd.startswith('ping '):
        ip = cmd[5:].strip()
        try:
            ping(ip, verbose=True)
        except RuntimeError:
            print(red('IP could not be found.'))
        print()

    elif cmd == 'echo':
        print('echo [message]')
        print('echo [message] > [filename]')

    elif cmd.startswith('echo '):
        msg = cmd[5:].strip()
        try:
            isWrite = msg.split('>')
            echoMsg = isWrite[0].strip()
            filename = isWrite[1].strip()
            filepath = (os.path.join(currentDir, filename)).replace('\\', '/')
            try:
                f = __builtins__.open(filepath, 'x')
                f.close()
                f = __builtins__.open(filepath, 'w')
                f.write(echoMsg)
                f.close()
            except FileExistsError:
                print(red(f'File "{filename}" already exists.'))
            except PermissionError:
                print(red('The program does not have permission to write this file.'))
            except OSError as a:
                print(red('The Humanity! An OSError occurred: {a}.'))
        except IndexError:
            print(msg)
        print()

    elif cmd == 'calc':
        print('calc [calculation]')
        print("use command 'calc help' to see available operations.")
        print('Sadly for now only supports simple expressions with 1 operator. Experimental evaluation support may be added soon.')
        print()

    elif cmd == 'calc help':
        print()
        print(red('== ARITHMETIC ==', 'bold'))
        print('Addition: x + y')
        print('Subtraction: x - y')
        print('Multiplication: x * y')
        print('Division: x / y')
        print('Remainder: x % y')
        print('Factorial: x!')
        print('Ceiling: ceil(x)')
        print('Floor: floor(x)')
        print()
        print(yellow('== EXPONENTS AND LOGARITHMS ==', 'bold'))
        print('Power: x ^ y')
        print('Square Root: sqrt(x)')
        print('Cube Root: cbrt(x)')
        print('Logarithm: log(x, base)')
        print()
        print(green('== TRIGONOMETRY ==', 'bold'))
        print('sine: sin(x)')
        print('cosine: cos(x)')
        print('tangent: tan(x)')
        print()

    elif cmd.find('+') != -1:
        nums = cmd.split('+')
        num1 = nums[0]
        num2 = nums[1]
        try:
            print(float(num1) + float(num2))
        except ValueError:
            print(red('Inputs must be a valid number'))
        except OverflowError:
            print(red('Number too large :('))
        print()

    elif cmd.find('-') != -1:
        nums = cmd.split('-')
        num1 = nums[0]
        num2 = nums[1]
        try:
            print(float(num1) - float(num2))
        except ValueError:
            print(red('Inputs must be a valid number'))
        except OverflowError:
            print(red('Number too large :('))
        print()

    elif cmd.find('*') != -1:
        nums = cmd.split('*')
        num1 = nums[0]
        num2 = nums[1]
        try:
            print(float(num1) * float(num2))
        except ValueError:
            print(red('Inputs must be a valid number'))
        except OverflowError:
            print(red('Number too large :('))
        print()

    elif cmd.find('/') != -1:
        nums = cmd.split('/')
        num1 = nums[0]
        num2 = nums[1]
        try:
            print(float(num1) / float(num2))
        except ValueError:
            print(red('Inputs must be a valid number'))
        except OverflowError:
            print(red('Number too large :('))
        except ZeroDivisionError:
            print('Cannot divide by zero.')
        print()

    elif cmd.find('%') != -1:
        nums = cmd.split('%')
        num1 = nums[0]
        num2 = nums[1]
        try:
            print(float(num1) % float(num2))
        except ValueError:
            print(red('Inputs must be a valid number'))
        except OverflowError:
            print(red('Number too large :('))
        print()

    elif cmd.find('^') != -1:
        nums = cmd.split('^')
        num1 = nums[0]
        num2 = nums[1]
        try:
            print(float(num1) ** float(num2))
        except ValueError:
            print(red('Inputs must be a valid number'))
        except OverflowError:
            print(red('Number too large :('))
        print()

    elif cmd.find('!') != -1:
        num = cmd.split('!')[0]
        try:
            print(m.factorial(int(num)))
        except ValueError:
            print(red('Inputs must be a valid number'))
        except OverflowError:
            print(red('Number too large :('))
        print()

    elif cmd.startswith('ceil('):
        num = cmd[5:].strip(')')
        try:
            print(m.ceil(float(num)))
        except ValueError:
            print(red('Inputs must be a valid number'))
        except OverflowError:
            print(red('Number too large :('))

    elif cmd.startswith('floor('):
        num = cmd[6:].strip(')')
        try:
            print(m.floor(float(num)))
        except ValueError:
            print(red('Inputs must be a valid number'))
        except OverflowError:
            print(red('Number too large :('))

    elif cmd.startswith('sqrt('):
        num = cmd[5:].strip(')')
        try:
            print(m.sqrt(float(num)))
        except ValueError:
            print(red('Inputs must be a valid number'))
        except OverflowError:
            print(red('Number too large :('))

    elif cmd.startswith('cbrt('):
        num = cmd[5:].strip(')')
        try:
            print(m.cbrt(float(num)))
        except ValueError:
            print(red('Inputs must be a valid number'))
        except OverflowError:
            print(red('Number too large :('))

    elif cmd.startswith('log('):
        nums = cmd[4:].strip(')')
        arguments = nums.split(',')
        try:
            num = arguments[0]
            base = arguments[1]
            try:
                print(m.log(float(num), float(base)))
            except ValueError:
                print(red('Inputs must be a valid number'))
            except OverflowError:
                print(red('Number too large :('))
        except IndexError:
            print(red('Incorrect Syntax. Use log(num, base).'))
        print()

    elif cmd.startswith('sin('):
        num = cmd[4:].strip(')')
        try:
            print(m.sin(float(num)))
        except ValueError:
            print(red('Inputs must be a valid number'))
        except OverflowError:
            print(red('Number too large :('))
        print()

    elif cmd.startswith('cos('):
        num = cmd[4:].strip(')')
        try:
            print(m.cos(float(num)))
        except ValueError:
            print(red('Inputs must be a valid number'))
        except OverflowError:
            print(red('Number too large :('))
        print()

    elif cmd.startswith('tan('):
        num = cmd[4:].strip(')')
        try:
            print(m.tan(float(num)))
        except ValueError:
            print(red('Inputs must be a valid number'))
        except OverflowError:
            print(red('Number too large :('))
        print()

    elif cmd == 'numguess':
        print('numguess [min], [max]')

    elif cmd.startswith('numguess '):
        print()
        nums = cmd[9:]
        minmax = nums.split(',')
        try:
            minimum = minmax[0]
            maximum = minmax[1]
            try:
                n = randint(int(minimum), int(maximum))
                print(f'Guessing a random number between {int(minimum)} and {int(maximum)}.')
                while True:

                    guess = input('Guess: ')
                    try:
                        guess = int(guess)
                    except ValueError:
                        print(red('Inputs must be a valid integer.'))
                        continue
                    if guess < n:
                        if guess < int(minimum):
                            print(f'Guess must be higher than {minimum}.')
                            continue
                        else:
                            print('Guess is too low!')
                            continue
                    elif guess > n:
                        if guess > int(maximum):
                            print(f'Guess must be lower than {maximum}.')
                            continue

                        else:
                            print('Guess is too high!')
                            continue
                    elif guess == n:
                        print('You guessed right!')
                        print()
                        break
            except ValueError:
                print(red('Inputs must be a valid integer.'))
                break
        except IndexError:
            print(red("Invalid syntax. Type 'numguess' for more syntax information."))

    elif cmd == 'weakshell' or cmd == 'ws':
        print()
        print('BLINDS OS WeakShell')
        print("Copyright (C) Vanity's Non Existent Corp. No Rights Reserved.")
        print('But for real, the actual license: MIT')
        print('Current Version: v1.0.0')
        print('Changelog: N/A')
        print('Optimizations: 0')
        print('Patches: 0')
        print('Feature Updates: 0')
        print('Commands Available: 22')
        print('Lines of code: 576')
        print('Optimizations: 0')
        print('GitHub: ')
        print()

    elif cmd == "":
        continue

    else:
        print(red("Unsupported command. Type 'help' for list of supported commands."))
        print()