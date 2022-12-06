from utils import read_file

values = read_file(6, str, False)

datastream = list(values[0])


def GetMarker(unique_characters):
    for i in range(len(datastream)):
        marker = ''
        for j in range(unique_characters):
            marker += datastream[i + j]
        if len(set(marker)) == unique_characters:
            print("Marker Index: " + str(i + unique_characters) + ", Packet: " + marker)
            break


GetMarker(4)
GetMarker(14)

# Part 1 = Marker Index: 1598, Packet: nmjl

# Part 2 = Marker Index: 2414, Packet: rmbvhnlstfpgzw
