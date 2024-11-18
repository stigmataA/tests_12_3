import unittest
import tests_12_3 as tests

rt_t = unittest.TestSuite()
rt_t.addTests((unittest.TestLoader().loadTestsFromTestCase(tests.RunnerTest)))
rt_t.addTests((unittest.TestLoader().loadTestsFromTestCase(tests.TournamentTest)))

runner = unittest.TextTestRunner(verboity=2))
runner.run(rt_t)