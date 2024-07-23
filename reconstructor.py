

def checksum(s, hash):
    prefix = s[:5]
    str_hash = str(hash)
    suffix = str_hash[-5:]
    prefix_val = sum(ord(c) for c in prefix)
    cs = prefix_val + int(suffix)
    
    return str(hash) + str(cs)


def string_hash(s):
    hash = 0
    for c in s:
        hash = (hash * 33 + ord(c)) % 0xFFFFFFFF
    return hash

def simple_hash(data):
    hash = string_hash(data)
    chash = checksum(data, hash)
    chash = chash.zfill(30)

    return chash



def reconstruct_data(fragments):
    # implementation of the reconstruct_data function
    indices = sorted(fragments.keys())
    reconstructed_data = ""

    for index in indices:
        if fragments[index]['hash'] == simple_hash(fragments[index]['data']):
            reconstructed_data += fragments[index]['data']
        else:
            return "Error: Data integrity verification failed."

    return reconstructed_data


fragments = {
    2: {'data': 'World', 'hash': simple_hash('World')},
    1: {'data': 'Hello', 'hash': simple_hash('Hello')},
    3: {'data': '!', 'hash': simple_hash('!')}
}
original_data = reconstruct_data(fragments)
print(fragments)
print(original_data)