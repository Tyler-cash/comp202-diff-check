import os


def main():
    current_dir = os.getcwd()
    stage = "stage1"
    dir_name = "run"

    # Instantiates directory
    run_dir = os.path.join(current_dir, stage, dir_name)

    # Deletes dir if it exists
    if os.path.exists(run_dir):
        os.removedirs(run_dir)
    os.makedirs(run_dir)
    print("Directory \"" + dir_name + "\" created")

    # Iterates through each stage and gets the command string, also the expected err and out
    commands = []
    err = []
    out = []
    for i in range(1, 10):
        file_name = "test" + str(i)
        file_location = os.path.join(current_dir, stage, file_name)
        with open(file_location + ".cmd") as file:
            commands.append(get_whole_file(file))
        with open(file_location + ".err") as file:
            err.append(get_whole_file(file))
        with open(file_location + ".out") as file:
            out.append(get_whole_file(file))


def get_whole_file(file):
    content = file.readlines()
    if len(content) is 0:
        return []
    else:
        return content


if __name__ == "__main__":
    main()
