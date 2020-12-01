list = open('input').read().split()
list = [int(num) for num in list]


def part_one():
    i = 0
    while i < len(list):
        j = i+1
        while j < len(list):
            print(f'Checking {i}, {j}')
            if list[i] + list[j] == 2020:
                print(f'soloution: {list[i]}, {list[j]} {list[i]*list[j]}')
                return 
            j+=1
        i+=1

def part_two():
    i = 0
    while i < len(list):
        j = i+1
        while j < len(list):
            k = j+1
            while k < len(list):
                print(f'Checking {i}, {j}, {k}')
                if list[i] + list[j] + list[k] == 2020:
                    print(f'soloution: {list[i]}, {list[j]}, {list[k]},  {list[i]*list[j]*list[k]}')
                    return 
                k+=1
            j+=1
        i+=1


part_two()
