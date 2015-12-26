import json

def value_of(blob):
    if type(blob) is dict:
        return value_of(blob.keys() + blob.values()) if "red" not in blob.values() else 0
    elif type(blob) is list:
        return sum(map(value_of, blob))
    elif type(blob) is int:
        return blob
    elif type(blob) is unicode:
        return 0
    else:
        print "unknown blob type", blob, type(blob)
        return 0


with open("day12.txt", "r") as f:
    s = f.read()

blob = json.loads(s)

print blob
print value_of(blob)