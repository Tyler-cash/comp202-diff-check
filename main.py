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

        command = get_whole_file(file_location + ".cmd")
        command = command.strip('\n')
        err = get_whole_file(file_location + ".err")
        out = get_whole_file(file_location + ".out")

        # Wipes test dir inside of run
        run_test_dir = os.path.join(run_dir, "test" + str(i))

        # Transfers contents of test directory to it's own directory inside of run
        test_dir = os.path.join(stage_dir, current_test)
        shutil.copytree(test_dir, run_test_dir)

        # Runs gcc and compiles c code defined by c_code_name variable
        subprocess.call("gcc " + c_code_name + ";", shell=True, env={"PATH": "/sbin:/bin:/usr/bin"})

        # copies compiled c_code_name inside of test directory inside of run
        shutil.copy(os.path.join(current_dir, "a.out"), run_test_dir)
        executable_dir = os.path.join(test_dir, "a.out")

        # shell_command = os.path.join(run_test_dir, "a.out") + " " + command + " > piped.out"
        os.chdir(run_test_dir)
        os.system("./a.out " + command + " > piped.out 2>piped.err")


def get_whole_file(file_path):
    with open(file_path) as file:
        content = file.read()
    if len(content) is 0:
        return []
    else:
        return content


if __name__ == "__main__":
    main()
