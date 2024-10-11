def matchingStrings(strings, queries):
    # Write your code here
    results = []
    for qu in queries:
        co = strings.count(qu)
        list.append(str(co))
    return results

strings = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']

print(matchingStrings(strings,queries))
