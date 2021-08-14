## Import the modules to handle JSON and YAML
import sys
import yaml
import json

with open(sys.argv[1], 'r') as f:
    contents = f.read()

data = contents.split('\n')

for chunk in data:
    if chunk.startswith(' ') and chunk.strip() != '':
        chunk_pieces = chunk.split(':')
        chunk_pieces.insert(0, '"')
        chunk_pieces[1] = chunk_pieces[1].strip()
        chunk_pieces.insert(2, '"')
        chunk_pieces.insert(3, ':')
        chunk_pieces.insert(4, ' "')
        chunk_pieces[5] = chunk_pieces[5].strip()
        chunk_pieces.append('"')
        print(' '*4 + ''.join(chunk_pieces))
    elif chunk.strip() == '':
        print('}')
    else:
        print(chunk + ' {')

print(data)
