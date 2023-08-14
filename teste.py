import json
manifest = 'files\manifest.json'
with open(manifest) as file:
    data = json.load(file)

print(len(data['Response']['jsonWorldContentPaths']['pt-br']))
