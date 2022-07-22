from unittest import TestCase
from src.core import BmiCalculator
from os.path import exists
import os


class TestBmiCalculator(TestCase):
    data = [
        {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
        {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
        {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
        {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
        {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
        {"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
    ]
    calculator = BmiCalculator(data)

    def test_calculate_bmi(self):
        h = 171
        w = 96
        bmi = 32.83
        self.assertEqual(self.calculator.calculate_bmi(w, h), bmi)

    def test_final_table(self):
        df = self.calculator.final_table()
        self.assertTrue(df.shape != (0, 0))

    def test_export_to_csv(self):
        self.calculator.export_to_csv(".")
        self.assertTrue(exists("./bmi_calculator.csv"))
        os.remove("./bmi_calculator.csv")


if __name__ == "__main__":
    TestBmiCalculator()
