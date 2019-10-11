#!/usr/bin/env python
import apb_rom

apb_uart = 0x00040000
apb_uart_brg = apb_uart | 4
apb_uart_hr  = apb_uart | 8

brg_config = 162
delay      = 1<<24
program = {}
program["code"] = []
program["code"] += [ (apb_rom.rom.op_set("increment",4),),
                     (apb_rom.rom.op_set("address",apb_uart_brg),),
                     (apb_rom.rom.op_req("write_arg",brg_config),),
                     (apb_rom.rom.op_set("address",apb_uart_hr),),
                     (apb_rom.rom.op_set("accumulator",64),),
                     (apb_rom.rom.op_req("write_acc",brg_config),("loop:",)),
                     (apb_rom.rom.op_alu("add",1),),
                     (apb_rom.rom.op_wait(delay),),
                     (apb_rom.rom.op_branch("branch",0),("loop",)),
                     ]
program["code"] += [
    (apb_rom.rom.op_finish(),),
    ]
compilation = apb_rom.rom.compile_program(program)
apb_rom.rom.mif_of_compilation(compilation)
