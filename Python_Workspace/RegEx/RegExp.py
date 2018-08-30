import re

# Match
matchobj = re.match(r'(.*)ta(.*)','Ekta Ekrtaas')

if matchobj:
    print(matchobj.group())                     # Entire match
    print(matchobj.group(1))                    # First parenthesis subgroup
    print(matchobj.group(2))                    # Second parenthesis subgroup
    print(matchobj.group(1,2))                  # Multiple subgroup
    print(matchobj.groups())                    # All subgroups


matchobj1 = re.match(r'(\d+)\.?(\d+)?', '12.43')

if matchobj1:
    print(matchobj1.groups())


# Search
searchobj1 = re.search(r'(.*)ta(.*)','Ekta Ekrtaas')

if searchobj1:
    print(searchobj1.groups())