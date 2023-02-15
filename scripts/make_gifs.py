import os 

my_dir = "results"

list_dir = os.listdir(my_dir)

for filename in list_dir:
    if "1_2_3" in filename:
        filepath = os.path.join(my_dir, filename)

        use_auto = 1 if "_u1_" in filename else 0

        my_mode = 3 if "m3" in filename else 0

        for my_file in os.listdir(filepath):
            for seed in [1,2,3]:
                if f"gen_99_s{seed}" in my_file and "npy" in my_file:
                    my_filepath = os.path.join(filepath, my_file)
                    print(my_filepath)

                    my_cmd = "python -m bevodevo.enjoy -n BackAndForthEnv-v0 -pi MLPBodyPolicy"\
                            f" -e 1 -a 1 -f {my_filepath} -u {use_auto} -m {my_mode} -g .3 -nr 1"\
                            " -s 1 -d 1"

                    print("enjoy command")
                    print(f"     {my_cmd}")
                    os.system(my_cmd)
