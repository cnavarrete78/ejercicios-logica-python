import io
import unittest
from contextlib import redirect_stdout

from ejercicios import CustomQueue, fizzbuzz, is_similar_to_zoo


class TestZoo(unittest.TestCase):

    def test_similares(self):
        for word in ['zoo', 'zzoooo', 'zzzoooooo', 'ZOO']:
            self.assertTrue(is_similar_to_zoo(word), word)

    def test_no_similares(self):
        for word in ['zzoo', 'zooo', 'z', 'oo', 'zozo', 'oozz', 'zoox', 'zoo ', '', None]:
            self.assertFalse(is_similar_to_zoo(word), word)


class TestCustomQueue(unittest.TestCase):

    def queue(self, queue_type, items=(1, 2, 3)):
        q = CustomQueue(queue_type)
        for item in items:
            q.add_item(item)
        return q

    def show(self, q):
        with redirect_stdout(io.StringIO()):
            return q.show_queue()

    def test_fifo(self):
        self.assertEqual(self.show(self.queue('FIFO')), [1, 2, 3])

    def test_lifo(self):
        self.assertEqual(self.show(self.queue('LIFO')), [3, 2, 1])

    def test_remove_fifo(self):
        q = self.queue('FIFO')
        self.assertEqual([q.remove_item() for _ in range(3)], [1, 2, 3])

    def test_remove_lifo(self):
        q = self.queue('LIFO')
        self.assertEqual([q.remove_item() for _ in range(3)], [3, 2, 1])

    def test_cola_vacia(self):
        with self.assertRaises(IndexError):
            CustomQueue().remove_item()

    def test_tipo_invalido(self):
        with self.assertRaises(ValueError):
            CustomQueue('PILA')


class TestFizzBuzz(unittest.TestCase):

    def test_primeros_15(self):
        esperado = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz',
                    '11', 'Fizz', '13', '14', 'FizzBuzz']
        self.assertEqual([fizzbuzz(n) for n in range(1, 16)], esperado)

    def test_conteos_1_a_100(self):
        salida = [fizzbuzz(n) for n in range(1, 101)]
        self.assertEqual(salida.count('FizzBuzz'), 6)
        self.assertEqual(salida.count('Fizz'), 27)
        self.assertEqual(salida.count('Buzz'), 14)


if __name__ == '__main__':
    unittest.main()
