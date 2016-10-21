import os

import shutil

import subprocess


def main():
    current_dir = os.getcwd()
    stage = "stage1"
    dir_name = "run"
    c_code_name = "dmake.c"

    # Instantiates directory
    run_dir = os.path.join(current_dir, stage, dir_name)

    # Deletes dir if it exists
    if os.path.exists(run_dir):
        shutil.rmtree(run_dir, ignore_errors=True)
    os.makedirs(run_dir)
    print("Directory \"" + dir_name + "\" created")

    # Compares output with each test
    for i in range(1, 10):
        current_test = "test" + str(i)
        command = ""
        err = ""
        out = ""
        stage_dir = os.path.join(current_dir, stage)
        file_location = os.path.join(stage_dir, current_test)
        with open(file_location + ".cmd") as file:
            command = get_whole_file(file)
        with open(file_location + ".err") as file:
            err = get_whole_file(file)
        with open(file_location + ".out") as file:
            out = get_whole_file(file)
        print("command, err and out successfully parsed for test" + str(i))

        # Wipes test dir inside of run
        run_test_dir = os.path.join(run_dir, "test" + str(i))

        # Transfers contents of test directory to it's own directory inside of run
        test_dir = os.path.join(stage_dir, current_test)
        shutil.copytree(test_dir, run_test_dir)
        print("Successfully copied " + current_test + " directory")

        # Runs gcc and compiles c code defined by c_code_name variable
        subprocess.call('gcc ' + c_code_name + "; pwd;", shell=True, env={'PATH': '/sbin:/bin:/usr/bin'})


def get_whole_file(file):
    content = file.readlines()
    if len(content) is 0:
        return []
    else:
        return content


if __name__ == "__main__":
    main()
