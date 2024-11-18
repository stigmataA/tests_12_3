import runner as r
import runner_and_tournament as rt
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсы заморожены")
    def test_walk(self):  # метод, в котором создаётся объект класса Runner с произвольным именем
        a = r.Runner(name='Ivan')  # создаём объект
        for i in range(10):  # вызов метода walk у этого объекта 10 раз
            a.walk()
        self.assertEqual(a.distance,
                         50)  # сравните distance этого объекта со значением 50 (assertEqual функция из модуля unittest, которая используется в модульном тестировании для проверки равенства двух значений)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсы заморожены")
    def test_run(self):  # метод, в котором создаётся объект класса Runner с произвольным именем
        a = r.Runner(name='Ivan')  # создаём объект
        for i in range(10):  # вызов метода run у этого объекта 10 раз
            a.run()
        self.assertEqual(a.distance, 100)  # сравние distance этого объекта со значением 100

    @unittest.skipIf(is_frozen, "Тесты в этом кейсы заморожены")
    def test_challenge(self):  # метод в котором создаются 2 объекта класса Runner с произвольными именами
        a = r.Runner(name='Ivan')  # создаём объект a
        b = r.Runner(name='Petr')  # создаём объект b
        for i in range(10):  # вызов метода walk и run у этих объектов 10 раз
            a.walk()
            b.run()
        self.assertNotEqual(a.distance,
                            b.distance)  # сравнение distance объектов a и b (assertNotEqual метод из модуля unittest, который проверяет, что два заданных значения не равны)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.runner1 = rt.Runner(name='Усейн', speed=10)
        self.runner2 = rt.Runner(name='Андрей', speed=9)
        self.runner3 = rt.Runner(name='Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(elem)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament1(self):
        t1 = rt.Tournament(90, self.runner1, self.runner3)
        t1_result = {k: str(v) for k, v in t1.start().items()}
        TournamentTest.all_results.append(t1_result)  # запись результатов в словарь all_results
        self.assertTrue(t1_result[2], 'Ник')  # сравнивается последний объект из all_resu

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament2(self):
        t2 = rt.Tournament(90, self.runner2, self.runner3)
        t2_result = {k: str(v) for k, v in t2.start().items()}
        TournamentTest.all_results.append(t2_result)  # запись результатов в словарь all_results
        self.assertTrue(t2_result[2],
                        'Ник')  # сравнивается последний объект из all_results и предполагаемое имя последнего бегуна (Ник)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament3(self):
        t3 = rt.Tournament(90, self.runner1, self.runner2, self.runner3)
        t3_result = {k: str(v) for k, v in t3.start().items()}
        TournamentTest.all_results.append(t3_result)  # запись результатов в словарь all_results
        self.assertTrue(t3_result[3], 'Ник')


if __name__ == "__main__":
    unittest.main()
