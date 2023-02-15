import os 

my_dir = "exp_results"

list_dir = os.listdir(my_dir)

for filename in list_dir:
    if "u" in filename:
        filepath = os.path.join(my_dir, filename)

        use_auto = 1 if "u1_" in filename else 0

        if "m3" in filename:
            my_mode = 3
        elif "m2" in filename:
            my_mode = 2
        elif "m1" in filename:
            my_mode = 1
        else:
            my_mode = 0

        for my_file in os.listdir(filepath):
            for seed in [13,17,19,23,29,31,37,39,100,200,300]:
                if f"gen_84_s{seed}" in my_file and "npy" in my_file:
                    my_filepath = os.path.join(filepath, my_file)
                    print(my_filepath)

                    my_cmd = "python -m bevodevo.enjoy -n BackAndForthEnv-v0 -pi MLPBodyPolicy"\
                            f" -e 1 -a 1 -f {my_filepath} -u {use_auto} -m {my_mode} -v 1 -nr 1"\
                            " -s 1 -d 0 -b 5"

                    print("enjoy command")
                    print(f"     {my_cmd}")
                    os.system(my_cmd)
