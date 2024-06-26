#modified registers dictionary with their address values

registers_Dictionary ={
    '00000': 'zero', '00001': 'ra', '00010': 'sp', '00100': 'tp', '00011': 'gp', 
    '00101': 't0', '00110': 't1', '00111': 't2', '01000': 's0', '01001': 's1', 
    '01010': 'a0', '01011': 'a1', '01100': 'a2', '01101': 'a3', '01110': 'a4', 
    '01111': 'a5', '10000': 'a6', '10001': 'a7', '10010': 's2', '10011': 's3', 
    '10100': 's4', '10101': 's5', '10110': 's6', '10111': 's7', '11000': 's8', 
    '11001': 's9', '11010': 's10', '11011': 's11', '11100': 't3', '11101': 't4', 
    '11110': 't5', '11111': 't6'
}


#define dictionaries for opcode and funct3 codes
opcode_dict = {
    "add": "0110011", "sub": "0110011", "sll": "0110011",
    "slt": "0110011", "sltu": "0110011", "xor": "0110011",
    "srl": "0110011", "or": "0110011", "and": "0110011",
    "lw": "0000011", "addi": "0010011", "sltiu": "0010011",
    "jalr": "1100111", "sw": "0100011", "beq": "1100011",
    "bne": "1100011", "blt": "1100011", "bge": "1100011",
    "bltu": "1100011", "bgeu": "1100011", "lui": "0110111",
    "auipc": "0010111", "jal": "1101111", "mul": "0110011",
    "rst": "0110111", "halt": "0110111", "rvrs": "0110111",
    "div": "0110011", "rem": "0110011",  
}


functions_dict = {
    "add": "000", "sub": "000", "sll": "001",
    "slt": "010", "sltu": "011", "xor": "100",
    "srl": "101", "or": "110", "and": "111",
    "lw": "010", "addi": "000", "sltiu": "011",
    "jalr": "000", "sw": "010", "beq": "000",
    "bne": "001", "blt": "100", "bge": "101",
    "bltu": "110", "bgeu": "111", "mul": "000",
    "rst": "000", "halt": "001", "rvrs": "010",
    "div": "100", "rem": "110",  
}




reg_value = {
    "zero": 0, "ra": 0, "sp": 0, "tp": 0, "gp": 0, 
    "t0": 0, "t1": 0, "t2": 0, "fp": 0, "s0": 0, 
    "s1": 0, "a0": 0, "a1": 0, "a2": 0, "a3": 0, 
    "a4": 0, "a5": 0, "a6": 0, "a7": 0, "s2": 0, 
    "s3": 0, "s4": 0, "s5": 0, "s6": 0, "s7": 0, 
    "s8": 0, "s9": 0, "s10": 0, "s11": 0, "t3": 0, 
    "t4": 0, "t5": 0, "t6": 0
}
