



def main():
    try:
        with open('input.txt', 'r') as f:
            content = f.read()
            result_one = part_one(content)
            print(f'The result for part one is {result_one}')

    except FileNotFoundError:
        print('unable to find file')
    

def part_one(content):
    input_list = parse_input(content)
    res = []

    for pair in input_list:
        first = int(pair[0])
        second = int(pair[1])
        for i in range(first, second+1, 1):
            if contains_invalid_ids(str(i)):
                res.append(i)
    return sum(res)


def parse_input(content):
    l = content.rstrip().split(',')
    return [pair.split('-') for pair in l]

def contains_invalid_ids(s):
    if len(s) % 2 == 1:
        return False
    for i in range(len(s)//2):
        if s[i] != s[i + (len(s)//2)]:
            return False
    return True

if __name__ == '__main__':
    main()

