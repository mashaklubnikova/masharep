from task_1 import Table, Tree, Facebook

if __name__ == "__main__":
    table = Table("wood", 1.0, 1.5)
    tree = Tree("pine", 10, 5.0)
    facebook = Facebook("Facebook", 100000, True)

    print("Объекты созданы успешно")

    print("Начало проверки методов с валидацией")
    try:
        table.change_height("a")
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
      table.change_height(-1.0)
    except TypeError as e:
      print(f"Ошибка: {e}")

    try:
      tree.grow("abc")
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
      tree.grow(-1)
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
      tree.get_carbon_storage("abc")
    except TypeError as e:
       print(f"Ошибка: {e}")

    try:
      tree.get_carbon_storage(-1)
    except ValueError as e:
       print(f"Ошибка: {e}")

    try:
        facebook.add_users("abc")
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
        facebook.add_users(-1)
    except ValueError as e:
        print(f"Ошибка: {e}")



    print("Начало проверки конструкторов с невалидными аргументами")

    try:
      table1 = Table(1, 1.0, 1.5)
    except TypeError as e:
       print(f"Ошибка: {e}")
    try:
      table1 = Table("wood", -1.0, 1.5)
    except ValueError as e:
      print(f"Ошибка: {e}")
    try:
      table1 = Table("wood", 1.0, -1.5)
    except ValueError as e:
        print(f"Ошибка: {e}")
    try:
      tree1 = Tree(1, 10, 5.0)
    except TypeError as e:
       print(f"Ошибка: {e}")
    try:
      tree1 = Tree("pine", -10, 5.0)
    except ValueError as e:
       print(f"Ошибка: {e}")
    try:
      tree1 = Tree("pine", 10, -5.0)
    except ValueError as e:
       print(f"Ошибка: {e}")
    try:
      facebook1 = Facebook(1, 10000, True)
    except TypeError as e:
      print(f"Ошибка: {e}")
    try:
      facebook1 = Facebook("Facebook", -10000, True)
    except ValueError as e:
      print(f"Ошибка: {e}")

