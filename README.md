# Only natively supports single C file projects 

#Automating the checking of the COMP202 assignment3
## How to use?
`git clone` the repository, then move the `test.py` and `input.py` script into the root of your COMP202 assignment 3 folder. This folder 
should contain a folder that's called `stageX`. Where X is the stage number defined in `input.py`. Also your C program should be specified 
in `c_code_name` also in `input.py` sample `input.py` is provided
## Assumed project structure
#### `input.py`
```
# Set this number to the stage
stage_number = 1
# Set this to what your C file is called (No dependency support, sorry)
c_code_name = "dmake.c"
```

#### Folder structure
``` 
./
├── CMakeLists.txt
├── dmake.c
├── test.py
├── stage1#Is the extracted stage folder provided 
|  ├── test1
|  ├── test2
|  ├──  etc
└──────────
```
Hopefully everything works~
