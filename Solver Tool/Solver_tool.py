import itertools
import math

target = float("585.36")

numbers = [
"""
5371.36
4507.28
2571.09
2231.8
1302.95
1226.05
1064.31
968.01
850.19
801.24
765.52
760.72
574.23
535.26
513.78
473.26
384.32
339.33
296.26
274.03
273.66
267.5
260.94
244.57
243.39
231.92
209.03
203.59
197.22
196.41
186.4
179.67
168.44
158.52
157.18
150.26
148
145.12
144.64
143.32
141.57
140.22
137.91
124.92
120.75
120.33
118.56
118.38
116.6
114.7
106.27
105.66
95.01
90.57
89.75
87.67
84.73
80.8
80.6
76.12
69.54
63.64
63.17
61.64
59.47
58.91
58.79
57.66
56.93
56.92
55.77
55.2
52.04
50.72
45.83
45.6
43.61
43.43
42.89
41
39.74
39.37
38.6
35.69
35.45
34.49
33.96
32.66
31.21
29.99
29.91
29.67
28.67
28.67
28.5
27.9
25.2
22.88
22.68
22.2
21.6
21.38
21.36
21.24
21.06
20.08
19.5
19.44
19.13
18.3
18.12
17.69
17.64
17.4
17.39
17.24
17.23
17.1
17.1
16.05
15.59
15.11
15
15
14.97
14.4
14.15
14.1
13.92
13.2
12.9
12
12
12
12
11.4
11.23
10.87
10.8
10.8
10.8
10.56
10.56
10.13
9.52
9.44
9.36
9
9
8.53
8.12
7.74
7.7
7.56
7.5
7.5
7.5
7.5
7.5
7.2
6.41
6
6
6
6
5.7
5.7
5.69
5.48
5.23
4.8
4.8
4.8
4.8
4.8
4.8
4.8
4.8
4.5
4.5
3.74
3.56
3.37
3
3
2.99
2.99
2.85
2.85
2.85
2.84
2.7
2.57
2.4
2.4
2.4
2.28
2.24
1.5
0.9
0.6
"""
]

# Replace new line character with comma
for x in numbers:
    add_comma = x.replace(",", "")
    # print("\nCommas removed from list: {}".format(add_comma))
    add_comma = add_comma.split('\n')
    # print("\nNew line characters removed and converted to list: {}".format(add_comma))
# Remove all blank strings from list
remove_empty_str = list(filter(None, add_comma))
# Remove all blank strings from list
remove_empty_str = list(filter(None, add_comma))
# If there is a negative sign at the end of a string in the list, move it to the front of the string
move_negative = ['-' + i[:-1] if i[-1] == '-' else i for i in remove_empty_str]
# Convert the list of strings to a list of floats
new_numbers = [float(i) for i in move_negative]

best_combination = ((None,))
best_result = math.inf
best_sum = 0

print("target:{}\nnumbers:{}".format(target,new_numbers))
# generate all combinations of the numbers
# including combinations with different lengths
for L in range(0, len(new_numbers)+1):
    if best_result == 0:
        break
    for combination in itertools.combinations(new_numbers, L):
        sum = 0
        for number in combination:
            sum += number
        result = target - sum
        if abs(result) < abs(best_result):
            best_result = result
            best_combination = combination
            best_sum = sum
            print("\nnew best\n{}\nsum:{} off by:{}".format(best_combination, best_sum, best_result))
            if best_result == 0:
                break

print("\nbest sum{} = {}".format(best_combination, best_sum))
