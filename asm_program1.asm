.section .data
    msg:
        .ascii "Hello, World\n"

.section .text
.global _start

_start:
    # print syscall
    movl $4, %eax
    movl $1, %ebx
    leal (msg), %ecx
    movl $13, %edx
    int $0x80


    # exit syscall
    movl $1, %eax
    movl $0, %ebx
    int $0x80
