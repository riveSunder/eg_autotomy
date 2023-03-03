import os 
import subprocess
from subprocess import check_output

dir_list = os.listdir("results")

my_output = "exp_0x01_eval.txt"

with open(my_output, "w") as f:
    f.writelines(["exp_0x01 eval summary\n"])


for folder in dir_list:
    if "_b16" in folder:

        my_path = os.path.join("results", folder)
        use_autotomy = 1 if "u1" in folder else 0


        enjoy_cmd = f"python -m bevodevo.enjoy -n BackAndForthEnv-v0"\
                f" -pi MLPBodyPolicy -e 3 -a 3 -f {my_path} -nr 1"\
                f" -u {use_autotomy}"

        print(enjoy_cmd)

        checked_output_a = check_output(enjoy_cmd.split())
        checked_output_b = str(checked_output_a)[2:-1]
        checked_output = checked_output_b.replace("\\n", "\n")

        with open(my_output, "a") as f:
            f.writelines(checked_output)


                
