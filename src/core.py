import pandas as pd


class BmiCalculator:
    def __init__(self, data=None):
        self.data = data

    def calculate_bmi(self, weight, height):
        """
        Calculate BMI using weight and height of person

        :param weight: person's weight
        :param height: person's height
        """
        BMI = weight / (height / 100) ** 2
        return round(BMI, 2)

    def final_table(self):
        """
        Calculate BMI category and Risk

        :return: pandas dataframe of the final results
        """
        for i in self.data:
            BMI = self.calculate_bmi(i["WeightKg"], i["HeightCm"])
            i["BMI"] = BMI
            if BMI <= 18.4:
                i["BMI Category"] = "Underweight"
                i["Health risk"] = "Malnutrition risk"
            elif BMI <= 24.9:
                i["BMI Category"] = "Normal weight"
                i["Health risk"] = "Low risk"
            elif BMI <= 29.9:
                i["BMI Category"] = "Overweight"
                i["Health risk"] = "Enhanced risk"
            elif BMI <= 34.9:
                i["BMI Category"] = "Moderately obese"
                i["Health risk"] = "Medium risk"
            elif BMI <= 39.9:
                i["BMI Category"] = "Severely obese"
                i["Health risk"] = "High risk"
            else:
                i["BMI Category"] = "Very severely obese"
                i["Health risk"] = "Very high risk"
        df = pd.DataFrame.from_dict(self.data)
        return df

    def number_of_overweigh(self):
        """
        Count the total number of overweight people
        """
        df = self.final_table()
        dd = df["BMI Category"].value_counts().to_dict()
        values = []
        for key, value in dd.items():
            if key in [
                "Overweight",
                "Moderately obese",
                "Severely obese",
                "Very severely obese",
            ]:
                values.append(value)
        return sum(values)

    def export_to_csv(self, path):
        """
        Export results to CSV

        :param path: path to store the file in
        :return: csv file in a given path
        """
        return self.final_table().to_csv(f"{path}/bmi_calculator.csv", index=False)
