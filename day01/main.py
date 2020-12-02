list = open('input').read().split()
list = [int(num) for num in list]


def part_one():
    i = 0
    while i < len(list):
        j = i + 1
        while j < len(list):
            if list[i] + list[j] == 2020:
                return list[i] * list[j]
            j += 1
        i += 1


def part_two():
    i = 0
    while i < len(list):
        j = i + 1
        while j < len(list):
            k = j + 1
            while k < len(list):
                if list[i] + list[j] + list[k] == 2020:
                    return list[i] * list[j] * list[k]
                k += 1
            j += 1
        i += 1

print(part_one())
print(part_two())
