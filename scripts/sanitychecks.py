from preflibtools.instances.preflibinstance import PreflibInstance
from preflibtools.instances.sanity import *

import os

IN_DIR = "../datasets/"
LOG_DIR = "../log/"

try:
    os.makedirs(LOG_DIR)
except FileExistsError as e:
    pass

with open(os.path.join(LOG_DIR, "log.html"), "w") as log_file:
    for ds_dir in os.listdir(IN_DIR):
        h1_written = False
        for file in os.listdir(os.path.join(IN_DIR, ds_dir)):
            if os.path.splitext(file)[1][1:] in ["soc", "toc", "soi", "toi"]:
                file_path = os.path.join(IN_DIR, ds_dir, file)
                instance = PreflibInstance(file_path)

                error_list_numbers = basic_numbers(instance)
                error_list_orders = orders(instance)
                if error_list_numbers or error_list_orders:
                    if not h1_written:
                        log_file.write("<h1>Dataset " + ds_dir + "</h1>")
                        h1_written = True
                    log_file.write("<h2>" + instance.file_name + " --- " + ds_dir + "</h2>")
                    if error_list_numbers:
                        log_file.write("<h3>Basic Numbers Check</h3>")
                        for error in error_list_numbers:
                            log_file.write("<p>" + str(error) + "</p>")
                    if error_list_orders:
                        log_file.write("<h3>Orders Check</h3>")
                        for error in error_list_orders:
                            log_file.write("<p>" + str(error) + "</p>")
