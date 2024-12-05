from collections import Counter


def read_file(path):
    with open(path, 'r') as file:
        for line in file:
            yield [int(a) for a in line.strip().split()]


a, b = zip(*read_file("d1a.txt"))

diff = [abs(int(a)-int(b)) for a, b in zip(sorted(a), sorted(b))]
print(f"Diff score {sum(diff)}")

counts_in_b = Counter(b)

print(f"Sim score {sum([i * counts_in_b.get(i, 0) for i in a])}")
