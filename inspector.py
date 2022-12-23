import csv

from inspection import Inspection


class Inspector:
    @staticmethod
    def get_inspections():
        inspections = []

        with open("data.csv", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            # Skip header.
            next(reader)

            for index, line in enumerate(reader):
                inspections.append(
                    Inspection(
                        inspection_id=line[0],
                        restaurant_name=line[1],
                        borough=line[2],
                        zipcode=line[5],
                        cuisine=line[7],
                        inspection_date=line[8],
                        violation_code=line[10],
                        violation_description=line[11],
                        score=line[13],
                        grade=line[14],
                        grade_date=line[15],
                    ),
                )

        return inspections
