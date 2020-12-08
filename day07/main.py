from pprint import pprint

bag_rules_input = open('input').read().split('\n')[:-1]

bag_rules_input_example = ['light red bags contain 1 bright white bag, 2 muted yellow bags.',
'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
'bright white bags contain 1 shiny gold bag.',
'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
'faded blue bags contain no other bags.',
'dotted black bags contain no other bags.']

bag_rules_other_example = [
        'shiny gold bags contain 2 dark red bags.',
'dark red bags contain 2 dark orange bags.',
'dark orange bags contain 2 dark yellow bags.',
'dark yellow bags contain 2 dark green bags.',
'dark green bags contain 2 dark blue bags.',
'dark blue bags contain 2 dark violet bags.',
'dark violet bags contain no other bags.',
]


def clean_up(br):
    clean_rules = {}
    for rule in br:
        rule = rule.replace('bags', '')
        rule = rule.replace('bag', '')
        rule = rule.replace(' ','')
        rule = rule.replace('.','')
        rs = rule.split('contain')
        if rs[1] == 'noother':
            clean_rules[rs[0]] = None
        else:
            bag_children = rs[1].split(',')
            clean_rules[rs[0]] = ([{"name": bag[1:], "quantity" : int(bag[0])} for bag in bag_children])
    return clean_rules


bag_rules = clean_up(bag_rules_other_example)

def is_child(parent, possible_child):
    if bag_rules[parent] == None:
        return False
    for child in bag_rules[parent]:
        if child["name"] == possible_child:
            return True
    return False


def get_list_of_all_parents(child):
    parents = []
    for bag in bag_rules:
        if is_child(bag, child):
            parents.append(bag)
    return parents


def get_all_ancestors(child):
    parents = get_list_of_all_parents(child)
    if len(parents) == 0:
        return parents
    for parent in parents:
        parents += get_all_ancestors(parent)
    return list(set(parents))


def find_all_children(top_rule, level=0):
    level += 1
    if top_rule == None:
        return
    for child in top_rule:
        find_all_children(bag_rules[child['name']], level)


pprint(find_all_children(bag_rules['shinygold']))

