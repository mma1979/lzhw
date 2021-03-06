from lzw_c import *

def glue_seq(seq, last_separate = False):
    if last_separate:
        s = seq.split()
        return " ".join(s[:-1]), s[-1]
    else:
        return " ".join(seq)

def code_filling(huff_codes):
    sequences = {}
    codes = {}
    for seq, code in huff_codes.items():
        cd = int("1" + code, 2)
        sequences[cd] = lzw_compress(seq)
        codes[seq] = code
    return sequences, codes

def huffman_decode(sequences, compressed):
    bitstring = bin(compressed)[2:]
    bit = ""
    for b in bitstring[1:]:  # after preceding 1
        bit += b
        bit_int = int("1" + bit, 2)
        if bit_int in sequences:
            yield lzw_decompress(sequences[bit_int])
            bit = ""

def org_shaping(seq, bits):
    org = " ".join(huffman_decode(seq, bits)).split()
    return [i.replace("__", " ") for i in org]