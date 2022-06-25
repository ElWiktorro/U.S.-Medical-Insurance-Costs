# importing csv library
import csv

# creating empty list for each column in insurance.csv
ages = []
sexes = []
bmis = []
childrens = []
smokers = []
regions = []
charges = []


# creating function which open insurance.csv and appending values to lists
def appending_rows(lst, column_name):
    with open('insurance.csv') as insurance_costs:
        insurance_dictreader = csv.DictReader(insurance_costs)

        for row in insurance_dictreader:
            lst.append(row[column_name])


# loading data from insurance.csv into lists using appending_rows function
appending_rows(ages, 'age')
appending_rows(sexes, 'sex')
appending_rows(bmis, 'bmi')
appending_rows(childrens, 'children')
appending_rows(smokers, 'smoker')
appending_rows(regions, 'region')
appending_rows(charges, 'charges')


# defining Medical Cost Dataset class and methods
class MedicalCostDataset:
    # using constructor giving new object dataset's attributes
    def __init__(self, ages, sexes, bmis, childrens, smokers, regions, charges):
        self.ages = ages
        self.sexes = sexes
        self.bmis = bmis
        self.childrens = childrens
        self.smokers = smokers
        self.regions = regions
        self.charges = charges
        print("You created patients_dataset instance of MedicalCostDataset including attributes such as:"
              "\n age,sex,bmi,children,smoker, region and charges")
        # rozdzielenie bo wedlug PEPa nie można takich długich lini mieć i zwieksza czytelność

    # finding out the average age of the patients in the dataset
    def fo_average_age(self):
        sum_of_ages = 0
        for age in self.ages:
            sum_of_ages += int(age)
        self.average_age = round(sum_of_ages / len(self.ages), 2)
        # albo zwracasz average_age samo, albo jak masz selfa to ja bym to dodal jako pole do klasy
        print("The average age of patients from this dataset is {}".format(self.average_age))
        return self.average_age

    # analyzing where a majority of the individuals are from
    def analyze_most_frequent_region(self):
        regions_dict = {}
        for region in self.regions:
            if not region in regions_dict:
                regions_dict[region] = 1
            else:
                regions_dict[region] += 1
        region_name = ''
        region_count = 0
        for key, value in regions_dict.items():
            if value > region_count:
                region_name = key
        self.most_frequent_region = region_name
        # albo zwracasz most_frequent_region samo, albo jak masz selfa to ja bym to dodal jako pole do klasy
        print("The majority of the individuals are from {this_region}".format(this_region=self.most_frequent_region))
        return self.most_frequent_region

    # looking at the different costs between smokers vs non smokers
    def costs_difference(self):
        sum_of_smokers_costs = 0
        sum_of_non_smokers_costs = 0
        for n in range(len(self.smokers)):
            if self.smokers[n] == 'yes':
                sum_of_smokers_costs += float(self.charges[n])
            else:
                sum_of_non_smokers_costs = float(self.charges[n])
        # tutaj nie wiem czy jest sens robić selfa, bo to zmienna pomocnicza
        self.average_for_smokers = sum_of_smokers_costs / self.smokers.count('yes')
        # tutaj nie wiem czy jest sens robić selfa, bo to zmienna pomocnicza i poprawka z tym sum_of_non
        self.average_for_non_smokers = sum_of_non_smokers_costs / self.smokers.count('no')
        # albo zwracasz averages_difference samo, albo jak masz selfa to ja bym to dodal jako pole do klasy
        self.averages_difference = round(self.average_for_smokers - self.average_for_non_smokers, 2)
        print('Difference between average insurance costs for smokers and non smokers is: {}'.format(
            self.averages_difference))

        return self.averages_difference

    # figuring out what the average age is for someone who has at least one child in dataset
    def parent_average_age(self):
        sum_of_age = 0
        counter = 0
        for n in range(len(self.childrens)):
            if int(self.childrens[n]) != 0:
                sum_of_age += int(self.ages[n])
                counter += 1
        self.parent_avg_age = round(sum_of_age / counter, 2)
        # albo zwracasz parent_avg_age samo, albo jak masz selfa to ja bym to dodal jako pole do klasy
        print("The average age for parent in this dataset is: " + str(self.parent_avg_age))
        return self.parent_avg_age


# creating instance of a MedicalCostDataset class
patients_dataset = MedicalCostDataset(ages, sexes, bmis, childrens, smokers, regions, charges)
