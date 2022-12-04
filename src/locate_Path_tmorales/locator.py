import os
import sys


def locator_searcher(repo_name):
    if not repo_name.isdigit():
        # vars
        new_path = ''
        entire_disk = os.getcwd()

        # si ejecuto el test desde cualquier posicion de cmd, y si no le paso custom params
        if not bool(entire_disk.__contains__(repo_name)) and len(sys.argv) == 1:
            arg_path = sys.argv[0]
            directories = arg_path.split('\\')

            for directory in directories:
                if directory == repo_name:
                    return sys.path.append(new_path[1:])
                else:
                    new_path = new_path + '\\' + directory

        # si digo especifocamente la ruta del repo un nivel arriba
        elif len(sys.argv) > 2 and sys.argv[1] == '--custom-path':
            custom_path = sys.argv[2]
            sys.path.append(custom_path)

        # si el disco donde estoy parado no tiene el repo ej: C:\automation
        elif entire_disk[:13] != entire_disk[:3] + repo_name:
            directories = entire_disk.split('\\')

            for directory in directories:
                if directory == repo_name:
                    return sys.path.append(new_path[1:])
                else:
                    new_path = new_path + '\\' + directory

        # por descarte el repo esta al lado del disco, C:\automation
        else:
            return sys.path.append(entire_disk[0:3])
    else:
        raise TypeError("The param for locator_searcher(repo_name) must be 'string'")
