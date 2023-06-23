class CompressedGene:
    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotipe!")

    def descompress(self) -> str:
        gene: str = ""

        for i in range(0,self.bit_string.bit_length()-1,2):
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene+= "A"
            elif bits == 0b01:
                gene+= "C"
            elif bits == 0b10:
                gene+="G"
            elif bits == 0b11:
                gene+="T"
            else:
                raise ValueError("Invalid Bits!")

        return gene[::-1]

    def __init__(self, gene: str) -> None:
        self._compress(gene)

if __name__ == "__main__":
    from sys import getsizeof
    original: str = "ACTGAACCTTGGACTGAACCTTGGACTGAACCTTGGACTGAACCTTGGACTGAACCTTGGACTGAACCTTGGACTGAACCTTGGACTGAACCTTGG"*100
    print("original: {}".format(getsizeof(original)))
    compressed : CompressedGene = CompressedGene(original)
    print("compressed: {}".format(getsizeof(compressed.bit_string)))
    print(compressed)
    print("original descomprimido: {}".format(original == compressed.descompress()))