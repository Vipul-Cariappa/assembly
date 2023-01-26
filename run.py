#!/usr/bin/python3

import argparse
import subprocess
from termcolor import cprint

def rm():
    args = [
        "rm",
        "./*.o",
        "./*.elf",
        # "./*.out",
    ]
    subprocess.run(" ".join(args), shell=True)

def compile_n_execute(filename: str, with_stdlib: bool):
    if filename.endswith(".asm"):
        filename = filename[0:-4]
    
    if not filename.startswith("./"):
        filename = "./" + filename

    # cprint(filename, "green")
    
    # as ./asm_program1.asm --32 -o ./asm_program1.o
    asm_args = [
        "as",
        f"{filename}.asm",
        "--32",
        "-o",
        f"{filename}.o"
    ]

    cprint("\n" + " ".join(asm_args), "green")
    result = subprocess.run(asm_args)

    if result.returncode != 0:
        exit(result.returncode)

    # gcc -o ./asm_program1.elf -m32 ./asm_program1.o -nostdlib
    gcc_args = [
        "gcc",
        "-o",
        f"{filename}.elf",
        "-m32",
        f"{filename}.o",
        "-nostdlib",
    ]

    if with_stdlib:
        gcc_args = gcc_args[:-1]

    cprint("\n" + " ".join(gcc_args), "green")
    result = subprocess.run(gcc_args)

    if result.returncode != 0:
        exit(result.returncode)

    # ./asm_program1.elf
    run_arg = [f"{filename}.elf"]
    
    cprint("\n" + " ".join(run_arg), "green")
    result = subprocess.run(run_arg)

    exit(result.returncode)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Filename of the file to compile and run", type=str)
    parser.add_argument("--withstdlib", help="Compile with stdlib. Make sure you have main entry point in the assembly", type=bool)
    args = parser.parse_args()
    
    if args.filename == "rm":
        rm()
    else:
        compile_n_execute(args.filename, args.withstdlib)
