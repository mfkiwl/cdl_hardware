#t apb_request
apb_request = {
    "paddr":32,
    "penable":1,
    "psel":1,
    "pwrite":1,
    "pwdata":32,
}

#t apb_response
apb_response = {
    "prdata":32,
    "pready":1,
    "perr":1,
}

#t apb_processor_response
apb_processor_response = {
    "acknowledge":1,
    "rom_busy":1,
}

#t apb_processor_request
apb_processor_request = {
    "valid":1,
    "address":16,
}

#t apb_rom_request
apb_rom_request = {
    "enable":1,
    "address":16,
}

#t timer_control
timer_control = {"reset_counter":1,
                 "enable_counter":1,
                 "block_writes":1,
                 "bonus_subfraction_numer":8,
                 "bonus_subfraction_denom":8,
                 "fractional_adder":4,
                 "integer_adder":8,
}

#t timer_value
timer_value = {"irq":1,
               "value":64,
}

#t i2c
i2c = {"scl":1, "sda":1}

#t i2c_conf
i2c_conf = {"divider":8, "period":8}

#t t_bit_delay_config 
bit_delay_config = { "load":1, "value":9}

#t t_bit_delay_response
bit_delay_response = { "load_ack":1, "value":9, "sync_value":1}

#t phase_measure_request
phase_measure_request = {"valid":1}

#t phase_measure_response
phase_measure_response = {"ack":1, "abort":1, "valid":1, "delay":9, "initial_delay":9, "initial_value":1}
