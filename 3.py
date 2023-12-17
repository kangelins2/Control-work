"""
Напишите генератор, который принимает 2 параметра
(Пусть это будет образно генератор который делит продукцию максимально поровну на склады)
1 - количество возвращаемых значений (складов)
2 - количество продукции (продукции)
Например 100 продукции на 5
-> 20
-> 20
-> 20
-> 20
-> 20
Или например
97 продукции на 5
-> 19
-> 19
-> 19
-> 20
-> 20
Порядок не важен, можно (20, 20, 19, 19, 19)
Или 2 на 3
-> 1
-> 1
-> 0
Чтобы проверить работу можно использовать функцию ниже

"""


def test(*args):
    for _ in range(5):
        yield 1


def check(func, a, b):
    print(sum(list(func(a, b))))


check(test, 5, 5)

def divide_products(num_products, num_warehouses):
  """
  Разделяет продукцию максимально поровну на склады.

  Args:
    num_products: Количество продукции.
    num_warehouses: Количество складов.

  Returns:
    Генератор, который возвращает количество продукции, отправленное на каждый склад.
  """

  if num_warehouses > num_products:
    num_warehouses = num_products
  remainder = num_products % num_warehouses
  products_per_warehouse = num_products // num_warehouses
  for i in range(num_warehouses):
    if i < remainder:
      yield products_per_warehouse + 1
    else:
      yield products_per_warehouse


def test_divide_products():
  """
  Проверяет работу генератора.
  """

  assert list(divide_products(100, 5)) == [20, 20, 20, 20, 20]
  assert list(divide_products(97, 5)) == [19, 19, 19, 20, 20]
  assert list(divide_products(2, 3)) == [1, 1, 0]


if __name__ == "__main__":
  test_divide_products()

products = divide_products(100, 5)
for product in products:
  print(product)