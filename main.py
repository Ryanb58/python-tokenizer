import os
import pprint
from collections import defaultdict

script_path = os.path.dirname(os.path.abspath(__file__))

tokens = defaultdict(int)

# Scan through every file in the 'test_files' directory.
for entry in os.scandir(script_path + '/test_files'):
    if not entry.name.startswith('.') and entry.is_file():
        # Opent he file.
        with open(script_path + '/test_files/' + entry.name) as fi:
            # Read the lines in the file.
            lines = fi.readlines()
            for line in lines:
                # lowercase and split on spaces. Check if alpha.
                words = [x for x in line.lower().split(' ')if x.isalpha()]

                for word in words:
                    # increment counter for word if we see it.
                    tokens[word] += 1

# Print it out in a beautiful form.
pprint.pprint(tokens)
