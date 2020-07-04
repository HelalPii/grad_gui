# global look up tables
medcineplace = {
        "0000": "defualt",
        "0001": None,
        "0010": None,
        "0011": None,
        "0100": None,
        "0101": None,
        "0110": None,
        "0111": None,
        "1000": None,
        "1001": None,
    }

MB_func={
    'take': '000' ,
    'manual': '001',
    'taken' : '010',
    'Ntaken' : '011',
    'full' : '100',
    'empty' : '101'
  } # this look up table for functions and commands with the medicine box packets

#=========================================================================================
def MB_MED_naming():
    global medcineplace

    #packet = input("packet:")
    split_string = packet.split("-", 10)

    boxs = [""]
    split_string = packet.split("-", 10)

    for x in range(0, 9):
        substring = split_string[x]
        boxs.append(substring)


    medcineplace['0000'] = boxs[0]
    medcineplace['0001'] = boxs[1]
    medcineplace['0010'] = boxs[2]
    medcineplace['0011'] = boxs[3]
    medcineplace['0100'] = boxs[4]
    medcineplace['0101'] = boxs[5]
    medcineplace['0110'] = boxs[6]
    medcineplace['0111'] = boxs[7]
    medcineplace['1000'] = boxs[8]
    medcineplace['1001'] = boxs[9]


def MB_packet_form(box,fun,ind):
    global MB_func,medcineplace
    pkt=None

    b = list(medcineplace.keys())[list(medcineplace.values()).index('cc')]
    pkt = f"{b}{MB_func[fun]}{ind}"
    #pkt=f"{medcineplace[box]}{MB_func[fun]}{ind}"    # temporary commented
    pkt_final=int(pkt, base=2)

    return pkt_final


#-----------------------main---------------------------------------------------------------------------------
MB_MED_naming()

# print(bin(MB_packet_form('b','manual',0)))
#
# print(type(MB_packet_form('b','manual',0)))

packets_array=bytearray(10) # create an array of bytes of size 10 : maximum number of doses per day =10
packets_array[0]= MB_packet_form('cc','manual',0)
print(packets_array)

