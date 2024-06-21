from collections import Counter


if __name__ == '__main__':
    s = input()
    counter_dict = dict(Counter(s))
    counter_dict = sorted(counter_dict.items(), key=lambda x: x[1], reverse=True)
    max_1_elements = 
    print(counter_dict)
