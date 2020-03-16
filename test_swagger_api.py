import unittest
import swagger

'''
Swagger API  test v0.3
'''


def status(r):
    return r.status_code


class SwaggerAPITest(unittest.TestCase):
    def test_01_get_petinfo01(self):
        "Получение информации о питомце, позитивный"
        self.assertEqual(status(swagger.pet(1)), 200)

    def test_02_get_petinfo02(self):
        "Получение информации о питомце, негативный - не найден"
        self.assertEqual(status(swagger.pet(600)), 404)

    def test_03_get_petinfo03(self):
        "Получение информации о питомце, негативный - Invalid ID supplied"
        self.assertEqual(status(swagger.pet("2+2")), 400)

    def test_04_post_pet_upd01(self):
        "Обновление информации о питомце, позитивный"
        self.assertEqual(status(swagger.pet_upd(1,"dog")), 200) 

    def test_05_post_pet_upd02(self):
        "Обновление информации о питомце, негативный"
        self.assertEqual(status(swagger.pet_upd(0,"cat")), 405) 
    def test_06_post_pet_upd03(self):
        "Обновление информации о питомце, Invalid ID"
        self.assertEqual(status(swagger.pet_upd("abc","frog")), 405) 


# тест в рамках ДЗ № 1

    def test_07_get_petstatus01(self):
        "Получение информации о питомцах по статусу, позитивный"
        self.assertEqual(status(swagger.pet_find("available")), 200)

    def test_08_get_petstatus02(self):
        "Получение информации о питомцах по статусу, негативный - несуществующий статус"
        self.assertEqual(status(swagger.pet_find("nodata")), 400)
  
    def test_09_get_petstatus03(self):
        "Получение информации о питомцах по статусу, негативный - Invalid status supplied"
        self.assertEqual(status(swagger.pet_find(11)), 400)

# тест в рамках ДЗ № 2

    def test_10_delete_pet01(self):
        "Удалить питомца, позитивный"
        self.assertEqual(status(swagger.pet_del(1)), 200)

    def test_11_delete_pet02(self):
        "Удалить питомца, негативный - не найден"
        self.assertEqual(status(swagger.pet_del(600)), 404)

    def test_12_delete_pet03(self):
        "Удалить питомца, негативный - Invalid ID supplied"
        self.assertEqual(status(swagger.pet_del("!1")), 400)


if __name__ == '__main__':
    unittest.main(verbosity=2)