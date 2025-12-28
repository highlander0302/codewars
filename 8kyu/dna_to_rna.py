INPUT_DNA_SEQ = "ACACACACCACTTTTTTTTTT"

""""Function assumes that the input is correct and only ACTG nucleotides are given."""


def dna_converter(dna):
    return dna.replace("T", "U")


RESULT = dna_converter(INPUT_DNA_SEQ)
print(RESULT)
