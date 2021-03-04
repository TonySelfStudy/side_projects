# Impractical python projects page # 15 "Poor Man's Bar Chart" exercise
import pprint

input_text = ("Like the castle in its corner in a medieval game,"
              + "I foresee terrible trouble And I stay here just the same")

my_dict = {}

for i in input_text.lower():
    if i not in my_dict.keys():
        my_dict[i] = [i]
    else:
        my_dict[i].append(i)

pp = pprint.PrettyPrinter(indent=2, compact=True,)
pp.pprint(my_dict)
