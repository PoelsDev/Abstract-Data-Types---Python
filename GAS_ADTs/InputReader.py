import os
from ADT_wrappers import BSTTableWrapper
from ADT_wrappers import ChainTableWrapper
from ADT_wrappers import QueueTableWrapper
from ADT_wrappers import StackTableWrapper
from ADT_wrappers import TwoThreeFourTreeTableWrapper
from DummyObject import DummyObject

def readInput(file):
    """
    +readInput() lees een inputfile en voert de commando's die daarin staan uit om: datatypes te creêren, .dot-files te creëren of om traverses te printen.
    :param file: Het bestand waarin de commando's zouden staan.
    Pre-condities: Het bestand moet commando's bevatten voor het maken van datatypes, het maken van .dot-files of het printen van traverses.
    Post-condities: De commando's in het bestand zullen uitgevoerd worden.
    """
    currentType = ""
    ADT = None
    printCount=0
    index=None
    with open(file, 'r') as inputfile:
        lines = inputfile.read().splitlines()
        for line in lines:
            if line.startswith("type"):
                type_properties = line.split("=")
                currentType = type_properties[1]
                if currentType == "hlin" or currentType == "23" or currentType == "heap" or currentType == "rb" or currentType == "hsep" or currentType == "hquad":
                    continue
                if type_properties[1].find(",") != -1:
                    split_properties = type_properties[1].split(",")
                    currentType = split_properties[0]
                    size = int(split_properties[1])
                    if currentType == "queue":
                        print(f"TYPE: {currentType}")
                        ADT = QueueTableWrapper(size)
                        printCount=1
                elif type_properties[1].find(",") == -1:
                    currentType = type_properties[1]
                    if currentType == "bst":
                        print(f"TYPE: {currentType}")
                        ADT = BSTTableWrapper()
                        printCount=1
                    elif currentType == "234":
                        print(f"TYPE: {currentType}")
                        ADT = TwoThreeFourTreeTableWrapper()
                        printCount=1
                    elif currentType == "stack":
                        print(f"TYPE: {currentType}")
                        ADT = StackTableWrapper()
                        printCount=1
                    elif currentType == "ll":
                        print(f"TYPE: {currentType}")
                        ADT = ChainTableWrapper()
                        printCount=1
                        index=0
            elif line.startswith("insert"):
                if currentType == "hlin" or currentType == "23" or currentType == "heap" or currentType == "rb" or currentType == "hsep" or currentType == "hquad":
                    continue
                insert_properties = line.split(" ")
                key = int(insert_properties[1])
                print(f"TYPE: {currentType} | Insert: {key}")
                if currentType == "bst" or currentType == "234" or currentType == "stack" or currentType == "queue":
                    ADT.tableInsert(DummyObject(key))
                elif currentType == "ll":
                    ADT.tableInsert(index, DummyObject(key))
                    index+=1
            elif line.startswith("delete"):
                if currentType == "hlin" or currentType == "23" or currentType == "heap" or currentType == "rb" or currentType == "hsep" or currentType == "hquad":
                    continue
                delete_properties = line.split(" ")
                if len(delete_properties) > 1:
                    key = int(delete_properties[1])
                    print(f"TYPE: {currentType} | delete: {key}")
                    if currentType == "bst":
                        ADT.tableDelete(DummyObject(key))
                    elif currentType == "234" or currentType == "ll":
                        ADT.tableDelete(key)

                else:
                    print(f"TYPE: {currentType} | delete")
                    if currentType == "stack":
                        print(ADT.tableDelete())
                    elif currentType == "queue":
                        ADT.tableDelete()
            elif line.startswith("print") and line.startswith("printsorted") is False:
                if currentType == "hlin" or currentType == "23" or currentType == "heap" or currentType == "rb" or currentType == "hsep" or currentType == "hquad":
                    continue
                if currentType == "234" or currentType == "bst" or currentType == "ll" or currentType == "stack" or currentType == "queue":
                    filename = currentType + "-" + str(printCount) + ".dot"
                    print(f"TYPE: {currentType} | ToDot: {filename}")
                    ADT.tablePrint(filename)
                    os.system(f"dot -Tps {filename} -o {currentType}-{str(printCount)}.ps")
                    printCount+=1
            elif line.startswith("printsorted"):
                if currentType == "hlin" or currentType == "23" or currentType == "heap" or currentType == "rb" or currentType == "hsep" or currentType == "hquad":
                    continue
                if currentType == "234" or currentType == "bst" or currentType == "ll":
                    print(f"TYPE: {currentType} | print sorted")
                    ADT.tableTraverse()
