from collections import deque


def is_similar_to_zoo(word):
    if not isinstance(word, str) or not word:
        return False

    word = word.lower()
    i, n = 0, len(word)
    while i < n and word[i] == 'z':
        i += 1
    z = i
    while i < n and word[i] == 'o':
        i += 1
    o = i - z

    return i == n and z > 0 and o == 2 * z


class CustomQueue:
    """class to manage custom queues according to given type
    """

    def __init__(self, queue_type='FIFO'):
        queue_type = str(queue_type).upper()
        if queue_type not in ('FIFO', 'LIFO'):
            raise ValueError('queue_type debe ser FIFO o LIFO')
        self.queue_type = queue_type
        self.items = deque()

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self):
        if not self.items:
            raise IndexError('la cola está vacía')
        if self.queue_type == 'FIFO':
            return self.items.popleft()
        return self.items.pop()

    def show_queue(self):
        items = list(self.items)
        if self.queue_type == 'LIFO':
            items.reverse()
        print(items)
        return items


def fizzbuzz(n):
    if n % 15 == 0:
        return 'FizzBuzz'
    if n % 3 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'
    return str(n)


if __name__ == '__main__':
    for word in ['zoo', 'zzoooo', 'zzoo', 'zozo']:
        print(word, is_similar_to_zoo(word))

    for queue_type in ['FIFO', 'LIFO']:
        q = CustomQueue(queue_type)
        for i in [1, 2, 3]:
            q.add_item(i)
        q.show_queue()

    for i in range(1, 101):
        print(fizzbuzz(i))
