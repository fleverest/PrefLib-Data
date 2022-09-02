import os

from preflibtools.instances.preflibinstance import PreflibInstance
from preflibtools.instances.convert import order_to_pwg

IN_DIR = "../datasets/"
OUT_DIR = "../trash/"

try:
    os.makedirs(OUT_DIR)
except FileExistsError as e:
    pass

for ds_dir in os.listdir(IN_DIR):
    if os.path.isdir(os.path.join(IN_DIR, ds_dir)):
        for file in os.listdir(os.path.join(IN_DIR, ds_dir)):
            if os.path.splitext(file)[1] in [".toi", ".toc", ".soi", ".soc"]:
                print("=================================")
                file_path = os.path.join(IN_DIR, ds_dir, file)
                print(file_path)
                instance = PreflibInstance(file_path)

                pwg_inst = PreflibInstance()
                pwg_str = order_to_pwg(instance)
                print(pwg_str)
                pwg_inst.parse_str(pwg_str, data_type='pwg', file_name=file)
                pwg_inst.write(os.path.splitext(file_path)[0] + '.pwg')
