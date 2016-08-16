#!/usr/bin/python

import sys

decode_dict = {
    161:'0',
    162:'1',
    163:'2',
    164:'3',
    165:'4',
    166:'5',
    167:'6',
    168:'7',
    169:'8',
    170:'9',
    171:'!',
    172:'?',
    173:'.',
    187:'A',
    188:'B',
    189:'C',
    190:'D',
    191:'E',
    192:'F',
    193:'G',
    194:'H',
    195:'I',
    196:'J',
    197:'K',
    198:'L',
    199:'M',
    200:'N',
    201:'O',
    202:'P',
    203:'Q',
    204:'R',
    205:'S',
    206:'T',
    207:'U',
    208:'V',
    209:'W',
    210:'X',
    211:'Y',
    212:'Z',
    213:'a',
    214:'b',
    215:'c',
    216:'d',
    217:'e',
    218:'f',
    219:'g',
    220:'h',
    221:'i',
    222:'j',
    223:'k',
    224:'l',
    225:'m',
    226:'n',
    227:'o',
    228:'p',
    229:'q',
    230:'r',
    231:'s',
    232:'t',
    233:'u',
    234:'v',
    235:'w',
    236:'x',
    237:'y',
    238:'z',
}

encode_dict = dict((v,k) for k,v in decode_dict.iteritems())


def decode(string):
    chars = [decode_dict[ord(byte)] for byte in string]
    return "".join(chars)

def encode(string):
    chars = [chr(encode_dict[byte]) for byte in string]
    return "".join(chars)


def usage():
    print "Usage:"
    print "%s d(ecode) <hex-string>" % sys.argv[0]
    print "%s D(ecode-reversed) <hex-string>"  % sys.argv[0]
    print "%s e(ncode) <string>"  % sys.argv[0]


def main():
    if len(sys.argv) != 3:
        print "ERROR: Invalid arguments count"
        usage()
        return

    flag = sys.argv[1]
    string = sys.argv[2]

    if flag == "d":
        print decode(string.decode("hex"))
    elif flag == "D":
        print "".join(reversed(decode(string.decode("hex"))))
    elif flag == "e":
        print encode(string).encode("hex")
    else:
        print "ERROR: Bad Flag"
        usage()


if __name__ == "__main__":
    main()
