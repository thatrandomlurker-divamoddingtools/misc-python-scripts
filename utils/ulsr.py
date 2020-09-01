#ulsr, stands for Undefined Length String Reader
#standard usage would simply be ulsr.reader('opened file name here'), it should read at the current offset)

bytes = []
strings = []

def reader(MMF):
    while True:
        byte = MMF.read(1)
        if byte == b'\x00':
            string = b''.join(bytes).decode('utf-8')
            bytes.clear()
            strings.append(string)
            break
        else:
            bytes.append(byte)
            
        
